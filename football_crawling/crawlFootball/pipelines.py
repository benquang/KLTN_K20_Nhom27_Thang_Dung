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
from google.cloud import storage
from datetime import datetime
# class CrawlfootballPipeline:
#     def process_item(self, item, spider):
#         return item
# class CustomCsvItemExporter(CsvItemExporter):
#     def _convert_value(self, value):
#         if isinstance(value, str):
#             return value
#         return super()._convert_value(value)
# class MultiCSVItemPipeline(object):
#     SaveTypes = ['fbref_MatchStats','fbref_MatchPlayerStats','fbref_MatchInfos','fbref_MatchGoals','fbref_MatchSquad']
#     def open_spider(self, spider):
#         self.files = dict([ (name, open('./fbref/'+name+'.csv','wb')) for name in self.SaveTypes ])
#         self.exporters = dict([ (name,CsvItemExporter(self.files[name],encoding = 'utf-8-sig')) for name in self.SaveTypes])
#         [e.start_exporting() for e in self.exporters.values()]

#     def close_spider(self, spider):
#         [e.finish_exporting() for e in self.exporters.values()]
#         [f.close() for f in self.files.values()]

#     def process_item(self, item, spider):
#         what = type(item).__name__
#         if what in set(self.SaveTypes):
#             self.exporters[what].export_item(item)
#         return item

class CustomCsvItemExporter(CsvItemExporter):
    def _convert_value(self, value):
        if isinstance(value, str):
            return value
        return super()._convert_value(value)

class MultiCSVItemPipeline(object):
    SaveTypes = ['fbref_MatchStats','fbref_MatchPlayerStats','fbref_MatchInfos','fbref_MatchGoals','fbref_MatchSquad']

    def __init__(self, gcs_bucket_name, gcs_credentials_path):
        self.gcs_bucket_name = gcs_bucket_name
        self.gcs_credentials_path = gcs_credentials_path

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            gcs_bucket_name=crawler.settings.get('GCS_BUCKET_NAME'),
            gcs_credentials_path=crawler.settings.get('GCS_CREDENTIALS_PATH')
        )

    def open_spider(self, spider):
        self.files = dict([ (name, open('./fbref/'+name+'.csv','wb')) for name in self.SaveTypes ])
        self.exporters = dict([ (name,CustomCsvItemExporter(self.files[name],encoding = 'utf-8-sig')) for name in self.SaveTypes])
        [e.start_exporting() for e in self.exporters.values()]

        self.storage_client = storage.Client.from_service_account_json(self.gcs_credentials_path)
        self.bucket = self.storage_client.get_bucket(self.gcs_bucket_name)

    def close_spider(self, spider):
        [e.finish_exporting() for e in self.exporters.values()]
        [f.close() for f in self.files.values()]

        # Upload files to GCS
        for name in self.SaveTypes:
            path_to_file = './fbref/'+name+'.csv'
            blob_name = name+'.csv'
            blob = self.bucket.blob(blob_name)
            blob.upload_from_filename(path_to_file)

    def process_item(self, item, spider):
        what = type(item).__name__
        if what in set(self.SaveTypes):
            self.exporters[what].export_item(item)
        return item


class GoogleCloudStoragePipeline:
    def __init__(self, bucket_name, service_account_key,folder_name):
        self.bucket_name = bucket_name
        self.service_account_key = service_account_key
        self.folder_name = folder_name
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        bucket_name = settings.get('GCS_BUCKET_NAME')
        service_account_key = settings.get('GCS_SERVICE_ACCOUNT_KEY')
        folder_name = settings.get('GCS_FOLDER_NAME')
        return cls(bucket_name, service_account_key, folder_name)

    def open_spider(self, spider):
        self.client = storage.Client.from_service_account_json(self.service_account_key)
        self.bucket = self.client.get_bucket(self.bucket_name)
        date_str = datetime.now().strftime('%Y-%m-%d')
        self.filename = f'{spider.name}_{date_str}.csv'
        self.file = open(self.filename, 'w', newline='')
        self.writer = None
        
    def close_spider(self, spider):
        self.file.close()
        blob = self.bucket.blob(f'{self.folder_name}/{self.filename}' if self.folder_name else self.filename)
        blob.upload_from_filename(self.filename)

    def process_item(self, item, spider):
        if self.writer is None:
            self.writer = csv.DictWriter(self.file, fieldnames=item.fields.keys())
            self.writer.writeheader()
        self.writer.writerow(dict(item))
        return item
    