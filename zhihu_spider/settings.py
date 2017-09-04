# -*- coding: utf-8 -*-

# Scrapy settings for zhihu_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu_spider'

SPIDER_MODULES = ['zhihu_spider.spiders']
NEWSPIDER_MODULE = 'zhihu_spider.spiders'

DOWNLOADER_MIDDLEWARES = {
'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
'scrapy_crawlera.CrawleraMiddleware': 600
}

CRAWLERA_USER = '26d6115db9134e78aea79cc22bb045ca'
CRAWLERA_PASS = 'zhounan800157'

DOWNLOAD_DELAY = 5

DEFAULT_REQUEST_HEADERS = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0",
"Accept":"text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding":"gzip, deflate, br",
"Connection":"keep-alive",
"authorization":"Bearer Mi4xSFNzREFBQUFBQUFBQUVJX0gxQkJEQmNBQUFCaEFsVk53bXJDV1FESXptbjV4amk3TnQ0MmFreVdqM1pHZVNiWXVn|1503321538|d61dfab276ad5d9d0afc2ac19e13ee51cdbd2ebd"
}


CRAWLERA_PRESERVE_DELAY = True

COOKIE = {
        "__utma": "51854390.1023158210.1504443916.1504443916.1504450207.2",
"__utmb": "51854390.0.10.1504450207",
"__utmc": "51854390",
"__utmv": "51854390.000--|3=entry_date=20170821=1",
"__utmz": "51854390.1504450207.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
"_xsrf": "e6b3d853-5950-4143-9336-d01c6be21540",
"_zap":	"2ad8d045-5acd-4bdf-88cd-2018a7a87a5f",
"aliyungf_tc": "AQAAAP6ZfX7EoAQATPZX32DfB7mkaxJF",
"cap_id": '"ZGNjNWUyMWVlOTliNGY2YTk0MzAxYmIzNGEzOTZjOGY=|1504450204|f7c4cdd120155500054f5eb7c2c61a80e6c7600b"',
"d_c0":	'"AEACFGNPQQyPTnNMfn4War_DPrOP1MI4Ryo=|1503321317"',
"q_c1":	"df75fb2a4fbb4207995a4febe8b3d962|1503321187000|1503321187000",
"q_c1":	"f5b6ab5d7cb848eebd518b1a50239826|1503321187000|1503321187000",
"r_cap_id":	'"ODYzNjFmYzBmMDE0NDExNTgxMDk2N2VmZTNlNDU4NDE=|1504450204|39dd01eb25cf113c4616f01f6d239288a0737ad2"',
"s-i": 16,
"sid": "2pf25ehu",
"s-q": "%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86%E6%80%8E%E4%B9%88%E5%AD%A6",
"z_c0": "Mi4xSFNzREFBQUFBQUFBUUFJVVkwOUJEQmNBQUFCaEFsVk5vNlBUV1FBTGNmNS1RYmE5aEt3aFBBTmN3SWJJclcxTUNB|1504450211|d3e5e9cabcd7abe934bb57c361cdd4bcf925cc78",
}


ITEM_PIPELINES = {
    'zhihu_spider.pipelines.ZhihuSpiderPipeline': 200,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False#不遵守Robot协议



# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu_spider.middlewares.ZhihuSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu_spider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihu_spider.pipelines.ZhihuSpiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
