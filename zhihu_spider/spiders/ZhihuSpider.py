# -*- coding: utf-8 -*-
import scrapy
import json
import codecs
from zhihu_spider.items import ZhihuSpiderItem
from zhihu_spider.pipelines import ZhihuSpiderPipeline

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/']
    loginUrl = 'https://www.zhihu.com/#signin'
    siginUrl = 'https://www.zhihu.com/login/email'

    custom_settings = {
        "COOKIES_ENABLED": True,
    }

    headers = {
        'Host':
        'www.zhihu.com',
        'Connection':
        'keep-alive',
        'Origin':
        'https://www.zhihu.com',
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Content-Type':
        'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'X-Requested-With':
        'XMLHttpRequest',
        'DNT':
        1,
        'Referer':
        'https://www.zhihu.com/',
        'Accept-Encoding':
        'gzip, deflate, br',
        'Accept-Language':
        'zh-CN,zh;q=0.8,en;q=0.6',
        'Upgrade-Insecure-Requests:':
        1,
    }

    cookies = {
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


    #feedUrl = 'http://www.zhihu.com/api/v4/members/shan-yang-yue/followers?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=0'
    feedUrl = "https://www.zhihu.com/api/v4/members/gong-qing-tuan-zhong-yang-67/answers?sort_by=created&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cvoting%2Cis_author%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=15&offset=0"
    #feedUrl = "http://www.zhihu.com/api/v4/answers/136133621/voters?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cfollower_count%2Cgender%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=10&offset=0"
    nextFeedUrl = ''
    curFeedId = 0

    def start_requests(self):
        return [
            scrapy.http.FormRequest(
                self.loginUrl,
                headers=self.headers,
                cookies=self.cookies,
                meta={'cookiejar': 1},
                callback=self.post_login)
        ]

    def post_login(self, response):
        xsrf = response.css(
            'div.view-signin > form > input[name=_xsrf]::attr(value)'
        ).extract_first()
        self.headers['X-Xsrftoken'] = xsrf

        return [
            scrapy.http.FormRequest(
                self.siginUrl,
                method='POST',
                headers=self.headers,
                meta={'cookiejar': response.meta['cookiejar']},
                formdata={
                    '_xsrf': xsrf,
                    'captcha_type': 'cn',
                    'email': 'xxx@xxx.com',
                    'password': 'xxxxx',
                },
                callback=self.after_login)
        ]

    def after_login(self, response):
        jdict = json.loads(response.body)
        print('after_login', jdict)
        if jdict['r'] == 0:
            z_c0 = response.headers.getlist('Set-Cookie')[2].split(';')[0].split('=')[1]
            self.headers['authorization'] = 'Bearer ' + z_c0
            return scrapy.http.FormRequest(
                url=self.feedUrl,
                method='GET',
                meta={'cookiejar': response.meta['cookiejar']},
                headers=self.headers,
                formdata={
                    'action_feed': 'True',
                    'limit': '10',
                    'action': 'down',
                    'after_id': str(self.curFeedId),
                    'desktop': 'true'
                },
                callback=self.parse)
        else:
            print(jdict['error'])


    def followee_follower(self,followee_follower_json):
        item = ZhihuSpiderItem()
        items = []
        item["totals"] = followee_follower_json["paging"]["totals"]
        item["next"] = followee_follower_json["paging"]["next"]
        items.append(item)
        return items


    def parse(self, response):
        # with codecs.open('test-2.json', 'a', encoding='utf-8') as fd:
        #     fd.write(response.body)
        jdict = json.loads(response.body)

        jdatas = jdict['data']
        for entry in jdatas:
            entry['pid'] = entry['id']
            yield entry

        jpaging = jdict['paging']
        self.curFeedId += len(jdatas)
        if jpaging['is_end'] == False and self.curFeedId < jdict['paging']['totals']:
            self.nextFeedUrl = jpaging['next']
            yield self.next_request(response)


    def next_request(self, response):
        return scrapy.http.FormRequest(
            url=self.nextFeedUrl,
            method='GET',
            meta={'cookiejar': response.meta['cookiejar']},
            headers=self.headers,
            callback=self.parse)

#test
