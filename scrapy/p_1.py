# -*- coding: utf-8 -*-
import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinkListsSpider(scrapy.Spider):
    name = 'project_1'
    allowed_domains = ['https://www.worlddata.info/']
    start_urls = ['https://www.worlddata.info/capital-cities.php']

    def parse(self, response):
        xpath = '//a[re:test(@class, "fl_.*")]//@href'
        selection = response.xpath(xpath)
        for s in selection[:100]:
            l = Link()
            l['link'] = 'https://www.worlddata.info' + s.get()
            yield l
    
