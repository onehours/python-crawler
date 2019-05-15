# -*- coding: utf-8 -*-
import scrapy
from downxiaoshuo.items import DownxiaoshuoItem

"""
下载凡人修仙传传小说，用scrapy不行 章节会乱
"""

class FanrenSpider(scrapy.Spider):
    name = 'fanren'
    # allowed_domains = ['www.www.com']
    start_urls = ['http://www.quanshuwang.com/book/0/269']

    def detail_url(self,response):
        print(response)
        # text = response.xpath('//div[@class="mainContenr"]/text()')
        text = response.xpath('//div[@id="content"]/text()').extract()
        item = DownxiaoshuoItem()
        item['name'] = response.meta['name']
        item['text'] = ''.join(text).replace('\r\n\xa0\xa0\xa0\xa0','')
        yield item

    def parse(self, response):
        print(response)
        li_list = response.xpath('//div[@class="clearfix dirconone"]/li')
        for li in li_list[:100]:
            url = li.xpath("./a/@href").extract_first()
            title = li.xpath("./a/@title").extract_first()
            print(title,url)
            yield scrapy.Request(url=url,callback=self.detail_url,meta={'name':title})