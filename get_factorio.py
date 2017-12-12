from html.parser import HTMLParser
import requests
import re

#
#
#  Scrape the factorio downloads page to collect the URL for the most recent 
#  server download.
#
#


#  URL for factorio website
base_url = 'https://www.factorio.com'

#  grab the HTML from the downloads page for parsing.
page=requests.get(base_url + '/download-headless')


#  Define parser, we're looking for links that reference the server file downloads

class FindLink(HTMLParser): 
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []


    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if re.match("/get-download/[\d.]+/headless/linux64",value):
                    self.data.append(value)


#  we only care about the most recent version of the server.

parser = FindLink()
parser.feed(page.text)
links = parser.data
links.sort()

#  return the URL.

print(base_url + links.pop())

# use curl -JLO $(python3 this_script) to get latest factorio. Hopefully
