#!python
# -*- coding: utf-8 -*-

# deviantArt Gallery Ripper
# http://lovecastle.org/dagr/
# https://github.com/voyageur/dagr

# Copying and distribution of this file, with or without
# modification, is permitted.

# This file is offered as-is, without any warranty.

import re
import sys
from getopt import gnu_getopt, GetoptError
from os import getcwd, makedirs
from os.path import (
    abspath, basename, exists as path_exists,
    expanduser, join as path_join
    )
from random import choice

try:
    # Python 3
    import configparser
except ImportError:
    # Python 2
    import ConfigParser as configparser

from robobrowser import RoboBrowser
from requests import codes as req_codes, session as req_session


# Helper functions
def da_make_dirs(directory):
    if not path_exists(directory):
        makedirs(directory)


# Main classes
class DagrException(Exception):
    def __init__(self, value):
        super(DagrException, self).__init__(value)
        self.parameter = value

    def __str__(self):
        return str(self.parameter)


class Dagr:
    """deviantArt gallery ripper class"""

    NAME = basename(__file__)
    __version__ = "0.64"
    MAX_DEVIATIONS = 1000000  # max deviations
    ART_PATTERN = (r"https://www\.deviantart\.com/"
                   r"[a-zA-Z0-9_-]*/art/[a-zA-Z0-9_-]*")

    def __init__(self):
        # Internals
        self.browser = None
        self.errors_count = dict()

        # Configuration
        self.directory = getcwd() + "/"
        self.mature = False
        self.overwrite = False
        self.reverse = False
        self.test_only = False
        self.verbose = False

        # Current status
        self.deviant = ""

    def load_configuration(self):
        my_conf = configparser.ConfigParser()
        # Try to read global then local configuration
        my_conf.read([expanduser("~/.config/dagr/dagr_settings.ini"),
                      path_join(getcwd(), "dagr_settings.ini")])
        if my_conf.has_option("DeviantArt", "MatureContent"):
            self.mature = my_conf.getboolean("DeviantArt", "MatureContent")
        if my_conf.has_option("Dagr", "OutputDirectory"):
            self.directory = abspath(
                expanduser(my_conf.get("Dagr", "OutputDirectory"))
                ) + "/"

    def start(self):
        if not self.browser:
            # Set up fake browser
            self.set_browser()

    def set_browser(self):
        user_agents = (
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1'
            ' (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.50'
            ' (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
            'Opera/9.99 (Windows NT 5.1; U; pl) Presto/9.9.9',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US)'
            ' AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2'
            ' (KHTML, like Gecko) Chrome/6.0',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; pl; rv:1.9.1)'
            ' Gecko/20090624 Firefox/3.5 (.NET CLR 3.5.30729)'
        )
        session = req_session()
        session.headers.update({'Referer': 'https://www.deviantart.com/'})
        if self.mature:
            session.cookies.update({'agegate_state': '1'})

        # Try to use lxml parser if available
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
        try:
            __import__("lxml")
            parser = "lxml"
        except ImportError:
            parser = "html.parser"
        # Workaround robobrowser bug https://github.com/jmcarp/robobrowser/issues/87
        if sys.version_info>=(3,5):
            re._pattern_type = re.Pattern

        self.browser = RoboBrowser(history=False, session=session,
                                   tries=3, user_agent=choice(user_agents),
                                   parser=parser)

    def get(self, url, file_name=None):
        if (file_name and not self.overwrite and
                path_exists(self.directory + file_name)):
            print(file_name + " exists - skipping")
            return
        self.browser.open(url)

        if self.browser.response.status_code != req_codes.ok:
            raise DagrException("incorrect status code - " +
                                str(self.browser.response.status_code))

        if file_name is None:
            return str(self.browser.parsed)
        else:
            # Open our local file for writing
            local_file = open(self.directory + file_name, "wb")
            # Write to our local file
            local_file.write(self.browser.response.content)
            local_file.close()

    def find_link(self, link):
        filelink = None
        mature_error = False
        self.browser.open(link)
        # Full image link (via download link)
        link_text = re.compile("Download( (Image|File))?")
        img_link = self.browser.get_link(text=link_text)
        if img_link and img_link.get("href"):
            self.browser.follow_link(img_link)
            filelink = self.browser.url
            return (basename(filelink), filelink)

        if self.verbose:
            print("Download link not found, falling back to direct image")

        # Fallback 1: try meta (filtering blocked meta)
        filesearch = self.browser.find("meta", {"property": "og:image"})
        if filesearch:
            filelink = filesearch['content']
            if basename(filelink).startswith("noentrythumb-"):
                filelink = None
                mature_error = True
        if not filelink:
            # Fallback 2: try collect_rid, full
            filesearch = self.browser.find("img",
                                           {"collect_rid": True,
                                            "class": re.compile(".*full")})
            if not filesearch:
                # Fallback 3: try collect_rid, normal
                filesearch = self.browser.find("img",
                                               {"collect_rid": True,
                                                "class":
                                                    re.compile(".*normal")})
            if filesearch:
                filelink = filesearch['src']

        if not filelink:
            if mature_error:
                if self.mature:
                    raise DagrException("maybe not an image")
                else:
                    raise DagrException("maybe a mature deviation/" +
                                        "not an image")
            else:
                raise DagrException("all attemps to find a link failed")

        filename = basename(filelink)
        return (filename, filelink)

    def handle_download_error(self, link, link_error):
        error_string = str(link_error)
        print("Download error (" + link + ") : " + error_string)
        if error_string in self.errors_count:
            self.errors_count[error_string] += 1
        else:
            self.errors_count[error_string] = 1

    def deviant_get(self, mode):
        print("Ripping " + self.deviant + "'s " + mode + "...")
        mode_arg = '_'
        if mode.find(':') != -1:
            mode = mode.split(':', 1)
            mode_arg = mode[1]
            mode = mode[0]

        # DEPTH 1
        pages = []
        for i in range(0, int(Dagr.MAX_DEVIATIONS / 24), 24):
            html = ""
            url = "https://www.deviantart.com/" + self.deviant.lower() + "/"

            if mode == "favs":
                url += "favourites/?catpath=/&offset=" + str(i)
            elif mode == "collection":
                url += "favourites/" + mode_arg + "?offset=" + str(i)
            elif mode == "scraps":
                url += "gallery/?catpath=scraps&offset=" + str(i)
            elif mode == "gallery":
                url += "gallery/?catpath=/&offset=" + str(i)
            elif mode == "album":
                url += "gallery/" + mode_arg + "?offset=" + str(i)
            elif mode == "query":
                url += "gallery/?q=" + mode_arg + "&offset=" + str(i)
            else:
                continue

            try:
                html = self.get(url)
            except DagrException:
                print("Could not find " + self.deviant + "'s " + mode)
                return

            prelim = re.findall(Dagr.ART_PATTERN, html,
                                re.IGNORECASE | re.DOTALL)

            c = len(prelim)
            for match in prelim:
                if match in pages:
                    c -= 1
                else:
                    pages.append(match)

            done = re.findall("(This section has no deviations yet!|"
                              "This collection has no items yet!)",
                              html, re.IGNORECASE | re.S)

            if len(done) >= 1 or c <= 0:
                break

            print(self.deviant + "'s " + mode + " page " +
                  str(int((i / 24) + 1)) + " crawled...")

        if not self.reverse:
            pages.reverse()

        if not pages:
            print(self.deviant + "'s " + mode + " had no deviations.")
            return
        else:
            try:
                da_make_dirs(self.directory + self.deviant + "/" + mode)
                if mode in ["query", "album", "collection"]:
                    da_make_dirs(self.directory + self.deviant + "/" +
                                 mode + "/" + mode_arg)
            except OSError as mkdir_error:
                print(str(mkdir_error))
                return
            print("Total deviations in " + self.deviant + "'s " +
                  mode + " found: " + str(len(pages)))

        # DEPTH 2
        counter2 = 0
        for link in pages:
            counter2 += 1
            if self.verbose:
                print("Downloading " + str(counter2) + " of " +
                      str(len(pages)) + " ( " + link + " )")
            filename = ""
            filelink = ""
            try:
                filename, filelink = self.find_link(link)
            except (KeyboardInterrupt, SystemExit):
                raise
            except DagrException as link_error:
                self.handle_download_error(link, link_error)
                continue

            if not self.test_only:
                try:
                    if mode in ["query", "album", "collection"]:
                        self.get(filelink, self.deviant + "/" +
                                 mode + "/" + mode_arg + "/" + filename)
                    else:
                        self.get(filelink, self.deviant + "/" +
                                 mode + "/" + filename)
                except DagrException as get_error:
                    self.handle_download_error(link, get_error)
                    continue
            else:
                print(filelink)

        print(self.deviant + "'s " + mode + " successfully ripped.")

    def group_get(self, mode):
        # TODO: merge duplicate code with deviant_get
        print("Ripping " + self.deviant + "'s " + mode + "...")

        url = 'https://www.deviantart.com/' + self.deviant.lower() + '/'
        if mode == "favs":
            url += "favourites/"
        elif mode == "gallery":
            url += "gallery/"

        folders = []

        i = 0
        while True:
            html = self.get(url + '?offset=' + str(i))
            k = re.findall('class="ch-top" href="' + url +
                           '([0-9]*/[a-zA-Z0-9_-]*)"',
                           html, re.IGNORECASE)
            if k == []:
                break

            new_folder = False
            for match in k:
                if match not in folders:
                    folders += k
                    new_folder = True
            if not new_folder:
                break
            i += 10

        # no repeats
        folders = list(set(folders))

        if not folders:
            print(self.deviant + "'s " + mode + " is empty.")
            return
        else:
            print("Total folders in " + self.deviant + "'s " +
                  mode + " found: " + str(len(folders)))

        if self.reverse:
            folders.reverse()

        pages = []
        for folder in folders:
            (folderid, label) = folder.split('/')
            for i in range(0, int(Dagr.MAX_DEVIATIONS / 24), 24):
                try:
                    html = self.get(url + folder + '?offset=' + str(i))
                except DagrException:
                    print("Could not find " + self.deviant + "'s " +
                          mode + " " + folder)
                    return

                prelim = re.findall(Dagr.ART_PATTERN, html,
                                    re.IGNORECASE | re.DOTALL)

                c = len(prelim)
                for match in prelim:
                    if match in pages:
                        c -= 1
                    else:
                        pages.append(match)

                done = re.findall("(This section has no deviations yet!|"
                                  "This collection has no items yet!)",
                                  html, re.IGNORECASE | re.S)

                if len(done) >= 1 or c <= 0:
                    break

                print("Page " + str(int((i / 24) + 1)) +
                      " in folder " + label + " crawled...")

            if not self.reverse:
                pages.reverse()

            try:
                da_make_dirs(self.directory + self.deviant + "/" +
                             mode + "/" + label)
            except OSError as mkdir_error:
                print(str(mkdir_error))
            counter = 0
            for link in pages:
                counter += 1
                if self.verbose:
                    print("Downloading " + str(counter) + " of " +
                          str(len(pages)) + " ( " + link + " )")
                filename = ""
                filelink = ""
                try:
                    filename, filelink = self.find_link(link)
                except (KeyboardInterrupt, SystemExit):
                    raise
                except Exception as link_error:
                    self.handle_download_error(link, link_error)
                    continue

                if not self.test_only:
                    try:
                        self.get(filelink, self.deviant + "/" +
                                 mode + "/" + label + "/" + filename)
                    except DagrException as get_error:
                        self.handle_download_error(link, get_error)
                        continue
                else:
                    print(filelink)

        print(self.deviant + "'s " + mode + " successfully ripped.")

    def print_errors(self):
        if self.errors_count:
            print("Download errors count:")
            for error in self.errors_count:
                print("* " + error + " : " + str(self.errors_count[error]))


def print_help():
    print(Dagr.NAME + " v" + Dagr.__version__ + " - deviantArt gallery ripper")
    print("Usage: " + Dagr.NAME +
          " [-d directory] " + "[-fgmhorstv] " +
          "[-q query_text] [-c collection_id/collection_name] " +
          "[-a album_id/album_name] " +
          "deviant1 [deviant2] [...]")
    print("Example: " + Dagr.NAME + " -gsfv derp123 blah55")
    print("For extended help and other options, run " + Dagr.NAME + " -h")


def print_help_detailed():
    print_help()
    print("""
Argument list:
-d, --directory=PATH
directory to save images to, default is current one
-m, --mature
allows to download mature content
-g, --gallery
downloads entire gallery
-s, --scraps
downloads entire scraps gallery
-f, --favs
downloads all favourites
-c, --collection=NUMERIC_ID/NAME
downloads specified favourites collection
 You need to specify both id and name (from the collection URL)
 Example: 123456789/my_favourites
-a, --album=NUMERIC_ID/NAME
downloads specified album
 You need to specify both id and name (from the album URL)
 Example: 123456789/my_first_album
-q, --query=QUERY_TEXT
downloads artwork matching specified query string
-t, --test
skips the actual downloads, just prints URLs
-h, --help
prints help and exits (this text)
-r, --reverse
download oldest deviations first
-o, --overwrite
redownloads a file even if it already exists
-v, --verbose
outputs detailed information on downloads

Proxies:
 you can also configure proxies by setting the environment variables
 HTTP_PROXY and HTTPS_PROXY

$ export HTTP_PROXY="http://10.10.1.10:3128"
$ export HTTPS_PROXY="http://10.10.1.10:1080"
""")


def main():
    gallery = scraps = favs = False
    collection = album = query = ""

    if len(sys.argv) <= 1:
        print_help()
        sys.exit()

    g_opts = "d:mu:p:a:q:c:vfgshrto"
    g_long_opts = ['directory=', 'mature',
                   'album=', 'query=', 'collection=',
                   'verbose', 'favs', 'gallery', 'scraps',
                   'help', 'reverse', 'test', 'overwrite']
    try:
        options, deviants = gnu_getopt(sys.argv[1:], g_opts, g_long_opts)
    except GetoptError as err:
        print("Options error: " + str(err))
        sys.exit()

    ripper = Dagr()
    ripper.load_configuration()

    for opt, arg in options:
        if opt in ('-h', '--help'):
            print_help_detailed()
            sys.exit()
        elif opt in ('-d', '--directory'):
            ripper.directory = abspath(expanduser(arg)) + "/"
        elif opt in ('-m', '--mature'):
            ripper.mature = True
        elif opt in ('-s', '--scraps'):
            scraps = True
        elif opt in ('-g', '--gallery'):
            gallery = True
        elif opt in ('-r', '--reverse'):
            ripper.reverse = True
        elif opt in ('-f', '--favs'):
            favs = True
        elif opt in ('-c', '--collection'):
            collection = arg.strip().strip('"')
        elif opt in ('-v', '--verbose'):
            ripper.verbose = True
        elif opt in ('-a', '--album'):
            album = arg.strip()
        elif opt in ('-q', '--query'):
            query = arg.strip().strip('"')
        elif opt in ('-t', '--test'):
            ripper.test_only = True
        elif opt in ('-o', '--overwrite'):
            ripper.overwrite = True

    print(Dagr.NAME + " v" + Dagr.__version__ + " - deviantArt gallery ripper")
    if deviants == []:
        print("No deviants entered. Exiting.")
        sys.exit()
    if not any([gallery, scraps, favs, collection, album, query]):
        print("Nothing to do. Exiting.")
        sys.exit()

    # Only start when needed
    ripper.start()

    for deviant in deviants:
        group = False
        try:
            html = ripper.get('https://www.deviantart.com/' + deviant + '/')
            deviant = re.search(r'<title>.[A-Za-z0-9-]*', html,
                                re.IGNORECASE).group(0)[7:]
            deviant = re.sub('[^a-zA-Z0-9_-]+', '', deviant)
            if re.search('<dt class="f h">Group</dt>', html):
                group = True
        except DagrException:
            print("Deviant " + deviant + " not found or deactivated!")
            continue
        if group:
            print("Current group: " + deviant)
        else:
            print("Current deviant: " + deviant)
        try:
            da_make_dirs(ripper.directory + deviant)
        except OSError as mkdir_error:
            print(str(mkdir_error))

        ripper.deviant = deviant
        if group:
            if gallery:
                ripper.group_get("gallery")
            if favs:
                ripper.group_get("favs")
            if any([scraps, collection, album, query]):
                print("Unsupported modes for groups were ignored")
                # TODO: support other queries / merge code
        else:
            if gallery:
                ripper.deviant_get("gallery")
            if scraps:
                ripper.deviant_get("scraps")
            if favs:
                ripper.deviant_get("favs")
            if collection:
                ripper.deviant_get("collection:" + collection)
            if album:
                ripper.deviant_get("album:" + album)
            if query:
                ripper.deviant_get("query:" + query)
    print("Job complete.")

    ripper.print_errors()


if __name__ == "__main__":
    main()

# vim: set tabstop=4 softtabstop=4 shiftwidth=4 expandtab:
