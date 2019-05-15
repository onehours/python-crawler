# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DownxiaoshuoPipeline(object):

    def open_spider(self,spider):
        print('开始爬虫')
        self.fp = open('./fanrenxiuxian.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        print('保存第{}章'.format(item['name']))

        # self.fp.write(item['name'])
        self.fp.write(item['text'])
        self.fp.write('\r\n')

        return item

    def close_spider(self,spider):
        print('结束爬虫')
        self.fp.close()