'''
Write program which reads a file with simple html code 
and removes all tags 
leaving only text 
(not a title, not a path to image or java script source). 
The result should be shown as found "visible" text lines printed out to the 
screen in right order
'''
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NAME = "text.file"
FILE = BASE_DIR+"//"+NAME

with open(FILE) as f:
    print f.readlines()

