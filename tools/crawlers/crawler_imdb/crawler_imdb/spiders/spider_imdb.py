import scrapy
import dateutil.parser
import string
import re
import time


class spider_imdb(scrapy.Spider):


    name = 'spider_imdb'

    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "CONCURENT_REQUESTS_PER_DOMAIN": 3,
        "HTTPCACHE_ENABLED": True
    }
    # Top list 
    #start_urls = ['https://www.imdb.com/chart/top?ref_=nv_mv_250_6', 'https://www.imdb.com/chart/moviemeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=JEAF9ET6W8Z8NN372NG9&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_2','https://www.imdb.com/chart/bottom?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=5K7RNK31A5X5WMGZ385S&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_8']
    # EACH DECADE
    start_urls = ['https://www.imdb.com/search/title/?release_date=1970,1979&title_type=feature',
                  'https://www.imdb.com/list/ls050597145/',
                  'https://www.imdb.com/list/ls000024359/',
                  'https://www.imdb.com/list/ls003017163/',
                  'https://www.imdb.com/list/ls003017163/',
                  'https://www.imdb.com/list/ls050429174/',
                  'https://www.imdb.com/list/ls055690375/',
                  'https://www.imdb.com/list/ls000586796/',
                  'https://www.imdb.com/list/ls070384164/',
                  'https://www.imdb.com/list/ls003657143/',
                  'https://www.imdb.com/list/ls057320455/',
                  'https://www.imdb.com/list/ls000094863/',
                  'https://www.imdb.com/list/ls063745866/',
                  'https://www.imdb.com/list/ls066803353/',
                  'https://www.imdb.com/list/ls056951143/',
                  'https://www.imdb.com/list/ls056951200/?ref_=otl_1',
                  'https://www.imdb.com/list/ls057271045/',
                  'https://www.imdb.com/list/ls000582536/',
                   'https://www.imdb.com/list/ls025652131/',
                   'https://www.imdb.com/list/ls053474382/',
                   'https://www.imdb.com/list/ls053417733/?ref_=otl_3',
                   'https://www.imdb.com/list/ls072492253/',
                   'https://www.imdb.com/search/title?release_date=1910,1919&sort=moviemeter&title_type=feature',
                   'https://www.imdb.com/list/ls053441566/']
    # TOP GROSS LISTS
    '''
    start_urls = ['https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=2&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=3&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=4&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=6&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=7&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=8&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=9&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=10&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=11&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=12&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=13&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=14&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=15&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=16&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=17&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=18&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=19&ref_=adv_nxt',
                  'https://www.imdb.com/search/title?title_type=feature&sort=boxoffice_gross_us,desc&page=20&ref_=adv_nxt',
                  ]
    '''
    # TOP GENRE LISTS
    '''start_urls =[ 'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_1&genres=action&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_2&genres=adventure&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_3&genres=animation&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_4&genres=biography&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_5&genres=comedy&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_6&genres=crime&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_7&genres=documentary&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_8&genres=drama&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_9&genres=family&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_10&genres=fantasy&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_11&genres=film_noir&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_12&genres=history&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_13&genres=horror&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_16&genres=mystery&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_17&genres=romance&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_18&genres=sci_fi&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_21&genres=thriller&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_22&genres=war&explore=title_type,genres',
                   'https://www.imdb.com/search/title?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cd28805a-4e91-4f0f-b066-0db5ff4dd1a7&pf_rd_r=87CXFWGQXAVT71THCMW8&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=boxoffice&ref_=chtbo_gnr_23&genres=western&explore=title_type,genres']
    '''
    
    base_url = 'https://www.imdb.com'
    
    def parse(self, response):
        top_list_xpath = '//td[@class="titleColumn"]/a/@href'
        genre_list_xpath = '//h3[@class="lister-item-header"]/a/@href' 


        for href in response.xpath(genre_list_xpath).extract():
            yield scrapy.Request(
                url='https://www.imdb.com' + href,
                callback=self.parse_film,
                meta={'url':'https://www.imdb.com' + href}
            )
        
        # Follow pagination links and repeat
        next_url = response.xpath(
            '//div[@class="nav"]/div[@class="desc"]/a/@href'
        ).extract_first()


        # print("NEXT -----",next_url)
        # print("\n\n\n\n\n\n\n\n")
    
        # yield scrapy.Request(
        #     url='https://www.imdb.com/search/title?' + next_url,
        #     callback=self.parse
        # )

    def parse_film(self, response):

        url = response.request.meta['url']

        title = (
            response.xpath('//h1[@itemprop="name"]/text()').extract_first()
            )

        link = response.xpath('//h1[@itemprop="name"]/span/a/text()')
        if link:
            year = ( response.xpath('//h1[@itemprop="name"]/span/a/text()').extract_first() )
        else:
            year = None

        link = response.xpath('//div[@class="subtext"]/text()')
        if link:
            mpaa_rating = ( link.extract()[1].replace("\n", " ").rstrip() )
        else:
            mpaa_rating = None

        link = response.xpath('//div[@class="titleReviewBar "]/div[@class="titleReviewBarItem"]/a/div[@class="metacriticScore score_favorable titleReviewBarSubItem"]/span/text()')
        if link:
            metacritic_rating = link.extract_first()
        else:
            metacritic_rating = None

        link = response.xpath('//div[@class="ratingValue"]/strong/span[@itemprop="ratingValue"]/text()')
        if link:
            imdb_rating = ( link.extract_first() )
        else:
            imdb_rating = None

        link = response.xpath('//div[@class="ratingValue"]/following-sibling::a/span/text()')
        if link:
            imdb_ratings_total = ( link.extract_first() )
        else:
            imdb_ratings_total = None
    
        link = response.xpath('//div[@class="titleReviewBarSubItem"]/div[contains(text(),"Popularity")]/following-sibling::div/span/text()')
        if link:
            imdb_popularity = ( link.extract_first().replace('\n','').replace('(','').rstrip().lstrip() )
        else:
            imdb_popularity = None
            print("POPULARITY NOT FOUND \n")
        
        link = response.xpath('//div[@class="titleReviewBarItem titleReviewbarItemBorder"]/div/span/a/text()')
        if link:
            imdb_user_reviews_total = ( link.extract()[0].replace('user','').rstrip() )
        else:
            imdb_user_reviews_total = None
        
        link = response.xpath('//div[@class="titleReviewBarItem titleReviewbarItemBorder"]/div/span/a/text()')
        if link:
            if len(link.extract()) > 1:
                imdb_critic_reviews_total = ( link.extract()[1].replace('critic','').rstrip() )
            else:
                imdb_critic_reviews_total = None
        else:
            imdb_critic_reviews_total = None
            
        link = response.xpath('//div[@class="txt-block"]/time[@itemprop="duration"]/text()')
        if link:
            runtime = ( link.extract_first().replace('min','').rstrip() )
        else:
            runtime = None
        
        link = response.xpath('//div[@itemprop="genre"]/a/text()')
        if link:
            genre =  ( ','.join(link.extract()).lstrip() )
        else:
            genre = None

        link = response.xpath('//div[@class="txt-block"]/h4[contains(text(),"Language")]//following-sibling::a/text()')
        if link:
            language = ( link.extract_first() )
        else:
            language = None

        link = response.xpath('//div[@class="txt-block"]/h4[contains(text(),"Country")]//following-sibling::a/text()')
        if link:
            country = link.extract_first()
        else:
            country = None

        link = response.xpath('//div[@class="txt-block"]/h4[contains(text(),"Release Date")]//following-sibling::text()')
        if link:
            release_date = ( link.extract_first().lstrip().replace('\n','').rstrip() )
        else:
            release_date = None
    
        link = response.xpath('//div[@class="txt-block"]/h4[contains(text(),"Production Co")]//following-sibling::span/a/span/text()')
        if link:
            production_co = ( link.extract_first() )
        else:
            production_co = None
    
        link = response.xpath('//div[@class="txt-block"]/h4[contains(text(),"Color")]//following-sibling::a/text()')
        if link: 
            color = link.extract_first()
        else:
            color = None
            
        link = response.xpath('//div[@itemprop="description"]/p/text()')
        if link:
            description = link.extract_first().rstrip().replace('\n','')
        else:
            description = None

        link = response.xpath('//div[@class="poster"]/a/img/@src')
        if link:
            poster_image = link.extract_first()
        else: 
            poster_image = None
        
        link = response.xpath('//div[@class="credit_summary_item"]/span/a/span/text()')
        if link:
            director = link.extract_first()
        else:
            director = None

        link = response.xpath('//table[@class="cast_list"]/tr/td[@itemprop="actor"]/a/span/text()')
        if link:
            cast = ( ','.join(link.extract()) ) 
        else:
            cast = None

        link = response.xpath('//div[@class="txt-block"]/h4[contains(text(),"Budget")]//following-sibling::text()')
        if link:
            budget = ( link.extract_first().replace('\n','').rstrip() )
        else:
            budget = None


        link = response.xpath('//div[@class="txt-block"]/h4[contains(text(),"Opening Weekend USA")]//following-sibling::text()')
        if link:
            gross_weekend_usa =  ( link.extract_first().replace('\n','').rstrip(',').lstrip() )
        else:
            gross_weekend_usa = None

        link = response.xpath('//div[@class="txt-block"]/h4[contains(text(),"Gross USA")]//following-sibling::text()')
        if link:
            gross_usa = ( link.extract_first().replace('\n','').rstrip().lstrip() )
        else:
            gross_usa = None

        link = response.xpath('//div[@class="txt-block"]/h4[contains(text(),"Cumulative Worldwide Gross")]//following-sibling::text()')
        if link: 
            gross_worldwide = ( link.extract_first().replace('\n','').rstrip().lstrip() )
        else:
            gross_worldwide = None

        yield {
            'title': clean_string(title),
            'year': year,
            'mpaa_rating': mpaa_rating,
            'metacritic_rating': metacritic_rating,
            'imdb_rating': imdb_rating,
            'imdb_ratings_total': imdb_ratings_total,
            'imdb_popularity': imdb_popularity,
            'imdb_user_reviews_total': imdb_user_reviews_total,
            'imdb_critic_reviews_total': imdb_critic_reviews_total,
            'runtime': runtime,
            'genre': genre,
            'language': language,
            'country': country,
            'release_date' : release_date.replace(r"\(.*\)",""),
            'production_co': production_co,
            'color' : color,
            'description' : description,
            'poster_image' : poster_image,
            'director': director,
            'cast': cast,
            'budget': budget,
            'gross_usa_weekend' : gross_weekend_usa,
            'gross_usa' : gross_usa,
            'gross_worldwide' : gross_worldwide
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