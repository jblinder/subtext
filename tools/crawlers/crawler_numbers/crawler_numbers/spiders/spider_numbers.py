import scrapy
import dateutil.parser
import string
import re
import time


class spider_numbers(scrapy.Spider):


    name = 'spider_numbers'

    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "CONCURENT_REQUESTS_PER_DOMAIN": 5,
        "HTTPCACHE_ENABLED": True
    }
    
    base_url = 'https://www.the-numbers.com/box-office-records/worldwide/all-movies/cumulative/all-time/'
    start_urls = ['https://www.the-numbers.com/box-office-records/worldwide/all-movies/cumulative/all-time']
    
    for i in range(6,50):
        s = base_url + str(i*100 + 1)
        start_urls.append(s)
    print(start_urls)


    def parse(self, response):
        root_url = 'https://www.the-numbers.com'

        for i,href in enumerate(response.xpath('//table/tbody/tr/td/following-sibling::td/following-sibling::td/b/a/@href').extract()):

            rank = response.xpath('//table/tbody/tr/td[@class="data"][1]/text()').extract_first()

            yield scrapy.Request(
                url= root_url+href,
                callback=self.parse_film,
                meta={'url':root_url+href,'rank': rank}
            )

        # Follow pagination links and repeat
        next_url = response.xpath(
            '//div[@class="nav"]/div[@class="desc"]/a/@href'
        ).extract_first()


    def parse_film(self, response):

        url = response.request.meta['url']
        rank = response.request.meta['rank']

        title                       = response.xpath('//div[@id="main"]/div/h1[@itemprop="name"]/text()').extract_first()
        numbers_gross_domestic      = response.xpath('//table[@id="movie_finances"]/tr/td/b[contains(text(),"Domestic Box Office")]/parent::td/parent::tr/td/following-sibling::td[@class="data"]/text()').extract_first()
        numbers_gross_international = response.xpath('//table[@id="movie_finances"]/tr/td/b[contains(text(),"International Box Office")]/parent::td/parent::tr/td/following-sibling::td[@class="data sum"]/text()').extract_first()
        numbers_gross_worldwide     = response.xpath('//table[@id="movie_finances"]/tr/td/b[contains(text(),"Worldwide Box Office")]/parent::td/parent::tr/td/following-sibling::td[@class="data"]/text()').extract_first()
        numbers_budget              = response.xpath('//td/b[contains(text(),"Budget")]/parent::td/parent::tr/td/following-sibling::td/text()').extract_first()
        year =  title[title.find("(")+1:title.find(")")]
        yield {
            'title': clean_string(title),
            'year': year,
            'numbers_worldwide_rank': rank,
            'numbers_gross_domestic': numbers_gross_domestic,
            'numbers_gross_international': numbers_gross_international,
            'numbers_gross_worldwide': numbers_gross_worldwide,
            'numbers_budget': numbers_budget
        }


def to_date(datestring):
    if datestring is None:
        return None
    date = dateutil.parser.parse(datestring)
    return date

def money_to_int(moneystring):
    if moneystring is None:
        return None
    moneystring = moneystring.replace('$', '').replace(',', '')
    return int(moneystring)

def runtime_to_minutes(runtimestring):
    if runtimestring is None:
        return None
    runtime = runtimestring.split()
    try:
        minutes = int(runtime[0])*60 + int(runtime[2])
        return minutes
    except:
        return None

def clean_string(input_string):
    printable = set(string.printable)
    clean=[s for s in input_string if s in printable]
    return ''.join(clean)
