import scrapy
import dateutil.parser
import string
import re
import time
import csv


class spider_podnapisi(scrapy.Spider):
    name = 'spider_podnapisi'

    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }
    start_urls = []
    with open("../../../../../data/unfound_subtitle_urls-2018-04-21-1206.csv") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]

        for d in data:         
            print(int(d['year'])+5)
            url = 'https://www.podnapisi.net/en/subtitles/search/advanced?keywords='+d['title']+'&year='+str(int(d['year'])-5)+'-'+str(int(d['year'])+5)+'&sort=stats.downloads&order=desc#list'
            start_urls.append(url)

    def parse(self, response):
        link = response.xpath('//table[@class="table table-striped table-hover"]/tbody/tr/td/div[@class="pull-left"]/following-sibling::span[@class="flags"]/i[not(contains(@class,"fa-eye-slash"))]/parent::*/parent::td/div[@class="pull-left"]/a[1]/@href')
        if link:
            download_link = link.extract_first()
        else: 
            download_link = None
            print("CANNOT FIND",download_link)

        link = response.xpath('//table[@class="table table-striped table-hover"]/tbody/tr/td/div[@class="pull-left"]/a[1]/@href')
        if link:
            download_link_alternate = link.extract_first()
        else: 
            download_link_alternate = None
            print("CANNOT FIND",download_link)

        link = response.xpath('//table[@class="table table-striped table-hover"]/tbody/tr/td/a/text()')
        if link:
            title = link.extract_first().replace('\n','').rstrip().lstrip().replace(r"\(.*\)","")
        else:
            title = None
            print("CANNOT FIND TITLE")            

        time.sleep(4)

        yield {
            'title': title,
            'url': download_link,
            'url2' : download_link_alternate
        }