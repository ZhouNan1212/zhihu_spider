# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import psycopg2#连接PostgreSQL的模块
from scrapy import log
import sys
reload(sys)
sys.setdefaultencoding("utf-8")



class ZhihuSpiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('test-1.json', 'a', encoding='utf-8')


    def process_item(self, item, spider):#将数据存储到json中
        line = json.dumps(dict(item), ensure_ascii=False, encoding='utf-8') + "\n"
        self.file.write(line)
        return item


    # def process_item_PostgreSQL(self,item, spider):#将数据存储到PostgreSQL中
    #     conn = psycopg2.connect(database="zhihu", user="postgres", password="zhounan800157", host="127.0.0.1", port="5432")
    #
    #     try:
    #         cur=conn.cursor()
    #             #self.conn.query(sql_desc)
    #             #cur.execute("INSERT INTO ewrrw values(dict(item));")
    #         cur.execute("""INSERT INTO postgresql_1
    #             (paging, totals, headline)
    #             VALUES(%s, %s, %s);""",
    #             (item['paging'],
    #             item['totals'],
    #             item['headline']))
    #
    #         conn.commit()
    #         log.msg("Data added to PostgreSQL database!",
    #             level=log.DEBUG,spider=spider)
    #
    #     except Exception, e:
    #         print 'insert record into table failed'
    #         print e
    #
    #     finally:
    #         if cur:
    #             cur.close()
    #     conn.close()
    #     return item


    def spider_closed(self, spider):
        self.file.close()

