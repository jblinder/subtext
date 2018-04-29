import string
import re
import time
import csv
import difflib
import urllib.request
import os
import zipfile
from os import listdir
from os.path import isfile, join

''' Locally unzip file'''
download_path = '../../../data/srt/'
def unzip_file(film_title):
    for file in os.listdir(download_path):
        if file.endswith(".zip"):
            filename = os.path.join(download_path, file)
            unzip(filename,film_title)
    
''' Rename unzipped srt file / zip file and mov to seperate folders'''
def unzip(filename,film_title):
    # unzip file to srt dir
    zip_ref = zipfile.ZipFile(filename, 'r')
    zip_ref.extractall(download_path)
    zip_ref.close()

    # move zip to archive folder
    os.rename(filename, download_path+"archive/"+film_title.replace(' ','-').replace(':','')+'.zip')

    # get unzipped srt file
    srtfile = None
    for file in os.listdir(download_path):
        if file.endswith(".srt"):
            srtfile = os.path.join(download_path, file)
            os.rename(srtfile , download_path + "srt/"+film_title.replace(' ','-').replace(':','')+'.srt')
    time.sleep(1)
# use this: difflib.get_close_matches
# first merge the two imbdb and srt csvs
movies = []
with open("../../../data/parsed_subtitle_urls-2018-04-21-1206.csv") as f:
    reader = csv.DictReader(f)
    movies = [r for r in reader]
    for m in movies:
        ftitle = m['title'] + " " + m['year']
        print(m['title'],m['url'])
        try:
            urllib.request.urlretrieve(m['url'], download_path +(ftitle + ".zip") ) 
        except:
            print ("error")
            continue # continue to next row
        
        time.sleep(2)
        unzip_file(ftitle)


