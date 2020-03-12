import urllib.request
from html.parser import HTMLParser
import json

def scratch_html(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    f = open("tmp.html", "w")
    f.write(html)
    f.close()
    return html


class ParseHtml(HTMLParser):
    flag = False
    intro_flag = False
    current_name = ""
    result = {}

    def handle_starttag(self, tag, attr):
        if tag == 'a' and self.flag:
            self.current_namename = attr[1][1]
            info = {
                'url': attr[0][1]
            }
            self.result[self.current_namename] = info
        elif tag == 'br' and self.flag:
            self.intro_flag = not self.intro_flag

    def handle_comment(self, data):
        if data == " .et_pb_column ":
            self.flag = False

    def handle_data(self, data):
        if data == "List of Modules":
            self.flag = True
        if self.flag and self.intro_flag:
            self.result[self.current_namename]['description'] = data.strip()

    def close(self):
        super().close()
        return self.result


html = ""
try:
    f = open("tmp.html", "r")
    html = f.read()
    f.close()
except OSError:
    html = scratch_html('http://www.computationalgenomics.ca/cvmfs-modules/')

parser = ParseHtml()
parser.feed(html)
with open("other.json", "w") as f:
    json.dump(parser.close(), f)