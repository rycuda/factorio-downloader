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
baseUrl = 'https://www.factorio.com'

#  grab the HTML from the downloads page for parsing.
page = requests.get(baseUrl + '/download-headless')

#  Define parser, we're looking for links that reference the server file downloads
class FindLink(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []


    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if re.match(r"/get-download/[\d.]+/headless/linux64", value):
                    self.data.append(value)


#  we only care about the most recent version of the server.

parser = FindLink()
parser.feed(page.text)
downloadLinks = parser.data
downloadLinks.sort()

#  return the URL.

print(baseUrl + downloadLinks.pop())

# use curl -JLO $(python3 this_script) to get latest factorio. Hopefully
