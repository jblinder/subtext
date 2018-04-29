import string
import re
import time
import csv
import difflib
import urllib


# use this: difflib.get_close_matches
# first merge the two imbdb and srt csvs
movies = []
with open("../../data/parsed_subs.csv") as f:
    reader = csv.DictReader(f)
    movies = [r for r in reader]
    srt = urllib.URLopener()
    for m in movies:
        srt.retrieve(m['url'], "files/" +(m['title'] + " " + m['year'] + ".zip") ) 
        time.sleep(1)
    
