# -*- coding: utf-8 -*-
import scrapy

class Countries(scrapy.Item):
    capital = scrapy.Field()
    name = scrapy.Field()
    region = scrapy.Field()
    area = scrapy.Field()
    local_name = scrapy.Field()
    exp = scrapy.Field()
    imp = scrapy.Field()
    death_penalty = scrapy.Field()
    birth_rate = scrapy.Field()
    roadways = scrapy.Field()
    airports = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'project_3'
    allowed_domains = ['https://www.worlddata.info/']
    try:
        with open("pt_1.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        p = Countries()

        capital_xpath        = '//*[text()="Capital:"]/following-sibling::div/text()'
        name_xpath        = '//h1/text()'
        region_xpath       = '//div[text()="Region:"]/following-sibling::*[1]/text()'
        area_xpath       = '//div[text()="Area:"]/following-sibling::*[1]/text()'
        local_name_xpath       = '//div[text()="Local name:"]/following-sibling::*[1]/text()'
        exp_xpath       = '//td[text()="Exportations:"]/following-sibling::*[1]/text()'
        imp_xpath       = '//td[text()="Importations:"]/following-sibling::*[1]/text()'
        death_penalty_xpath       = '//*[text()="Death penalty"]/parent::td/following-sibling::td/text()'
        birth_rate_xpath       = '//*[text()="Birthrate:"]/parent::div/text()'
        roadways_xpath       = '//*[text()="Roadways:"]/following-sibling::td/text()'
        airports_xpath       = '//*[text()="Airports"]/parent::td/following-sibling::td/text()'

        p['capital']        = response.xpath(capital_xpath).getall()
        p['name']        = response.xpath(name_xpath).getall()
        p['region']       = response.xpath(region_xpath).getall()
        p['area']       = response.xpath(area_xpath).getall()
        p['local_name']       = response.xpath(local_name_xpath).getall()
        p['exp']       = response.xpath(exp_xpath).getall()
        p['imp']       = response.xpath(imp_xpath).getall()
        p['death_penalty']     = response.xpath(death_penalty_xpath).getall()
        
        try:
        	p['birth_rate'] =  response.xpath(birth_rate_xpath).getall()[0]
        except:
        	p['birth_rate'] = ''
        	
        p['roadways']       = response.xpath(roadways_xpath).getall()
        p['airports']       = response.xpath(airports_xpath).getall()
        
        yield p
