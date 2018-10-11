from html.parser import HTMLParser
import re
import requests

#
#
#  Scrape the factorio downloads page to collect the URL for the most recent
#  server download.
#
#


#  URL for factorio website
BASE_URL = 'https://www.factorio.com'

#  grab the HTML from the downloads page for parsing.
PAGE = requests.get(BASE_URL + '/download-headless')

#  Define parser, we're looking for links that reference the server file downloads
class FindLink(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []


    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for dummy, value in attrs:
                if re.match(r"/get-download/[\d.]+/headless/linux64", value):
                    self.data.append(value)


#  we only care about the most recent version of the server.

PARSER = FindLink()
PARSER.feed(PAGE.text)
DOWNLOAD_LINKS = PARSER.data
DOWNLOAD_LINKS.sort()

#  return the URL.

print(BASE_URL + DOWNLOAD_LINKS.pop())

# use curl -JLO $(python3 this_script) to get latest factorio. Hopefully
