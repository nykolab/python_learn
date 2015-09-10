'''
Write program which reads a file with simple html code and removes all tags 
leaving only text (not a title, not a path to image or java script source). 
The result should be shown as found "visible" text lines printed out to the 
screen in right order
in_file = 
with open(in_file) as f:
    print f.readlines()


'''

import os

BASE_DIR = os.path.dirname(__file__)
print BASE_DIR
