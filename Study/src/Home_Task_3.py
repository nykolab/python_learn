'''
Write program which reads a file with simple html code 
and removes all tags leaving only text 
(not a title, not a path to image or java script source). 
The result should be shown as found "visible" text lines printed out to the 
screen in right order
'''
import os
from HTMLParser import HTMLParser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NAME = "text.file"
FILE = BASE_DIR+"//"+NAME
data_tags = ["title","b","br", "div", "tr","th"]
class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.record = False
        self.reset()
    def handle_starttag(self, tag, attrs):
        if tag.lower() in data_tags and not attrs:
            self.record = True
    def handle_data(self, data):
        if self.record == True: 
            print data
            

        
with open(FILE) as f:
    p = MyHTMLParser()
    html = f.read()
    p.feed(html)
    

