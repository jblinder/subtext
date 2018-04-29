import string
import re
import time
import csv
import difflib
import datetime

def timestamp_filename(fn,ext):
    return f"{fn}-{datetime.datetime.now():%Y-%m-%d-%I%M}.{ext}"

# use this: difflib.get_close_matches
# first merge the two imbdb and srt csvs
movies = []
with open("../../../data/imdb_unique_prod-2018-04-21_0924.csv") as f:
    reader = csv.DictReader(f)
    movies = [r for r in reader]


subtitles = []
with open("../../../data/sub_extraction-UNFOUND.csv") as f:
    reader = csv.DictReader(f)
    subtitles = [r for r in reader]

parsed_subs = []
bad_subs = []
for m in movies:
    title = m['title']
    year =  m['year']
    sub = [s for s in  subtitles if title in s['title'] and year in s['title']]
    
    sub_dict = {}
    if sub and len(sub) > 0:
        sub_dict['title'] = title.replace(':','-')
        if sub[0]['url']:
            sub_dict['url'] = 'https://www.podnapisi.net' +sub[0]['url']
        else:
            sub_dict['url'] = 'https://www.podnapisi.net' +sub[0]['url2']
        sub_dict['year'] = year
        parsed_subs.append(sub_dict)
    else:
        sub_dict['title'] = title.replace(':','-')
        sub_dict['year'] = year
        bad_subs.append(sub_dict)

for s in bad_subs:
    print(s['title'].split('-')[0])

keys = parsed_subs[0].keys()
with open(timestamp_filename('../../../data/parsed_subtitle_urls_FOUND','csv'), 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(parsed_subs)

keys = bad_subs[0].keys()
with open(timestamp_filename('../../../data/unfound_subtitle_urls_FOUND','csv'), 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(bad_subs)


#print(bad_subs)

#iterate through each movie and try to find in srt data-- if found, add exact name of moive (and id) to srt csv and then pop from film array

#save new srt array to csv

#save new delta array to csv

