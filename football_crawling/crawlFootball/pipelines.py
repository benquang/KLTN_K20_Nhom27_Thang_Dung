# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter
from scrapy import signals
from crawlFootball.items import *
import csv
class CrawlfootballPipeline:
    def process_item(self, item, spider):
        return item
class CustomCsvItemExporter(CsvItemExporter):
    def _convert_value(self, value):
        if isinstance(value, str):
            return value
        return super()._convert_value(value)
class MultiCSVItemPipeline(object):
    SaveTypes = ['fbref_MatchStats','fbref_MatchPlayerStats','fbref_MatchInfos','fbref_MatchGoals','fbref_MatchSquad']

    def open_spider(self, spider):
        self.files = dict([ (name, open('./fbref/'+name+'.csv','wb')) for name in self.SaveTypes ])
        self.exporters = dict([ (name,CsvItemExporter(self.files[name],encoding = 'utf-8-sig')) for name in self.SaveTypes])
        [e.start_exporting() for e in self.exporters.values()]

    def close_spider(self, spider):
        [e.finish_exporting() for e in self.exporters.values()]
        [f.close() for f in self.files.values()]

    def process_item(self, item, spider):
        what = type(item).__name__
        if what in set(self.SaveTypes):
            self.exporters[what].export_item(item)
        return item
    
