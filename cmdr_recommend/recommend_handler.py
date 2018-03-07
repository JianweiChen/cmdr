# coding=utf8
# 数据服务逻辑代码入口
from cmdr_recommend.idl.cmdr_recommend.CmdrRecommend import Iface
from cmdr_recommend.idl.cmdr_recommend.ttypes import RecommendResponse, RecommendRequest, Resource
import logging
import time
logging.basicConfig(filename="/var/log/cmdr/cmdr_recommend.log",level=logging.INFO)
import redis
import jieba
import json
import random
from collections import defaultdict

def get_dict_by_char(r, c):
    x = r.get(c)
    if not x:
        return {}
    else:
        return json.loads(x)

def update_dict_by_char(r, c, data):
    x = get_dict_by_char(r,c)
    x.update(data)
    r.set(c, json.dumps(x))

def get_data(r, url):
    x = r.get(url)
    if not x:
        return None
    else:
        return json.loads(x)
def set_data(r, url, data):
    r.set(url, json.dumps(data))

def get_c(text):
    if not isinstance(text, unicode):
        text = text.decode('utf8')
    stop_words = set()
    with open("/opt/cmdr/cmdr_recommend/word", 'r') as r:
        for line in r:
            c = line.strip().decode('utf8')
            stop_words.add(c)
    seg_list = list(jieba.cut_for_search(text))
    char_list = [c for c in text]
    seg_list = [s for s in seg_list if s not in stop_words]
    seg_list.extend(char_list)
    seg_map = defaultdict(int)
    for s in seg_list:
        seg_map[s] += 1
    return  seg_map

def get_rsp(text):
    # 只需要调用这个函数就能返回数据给前端，工作也就结束了
    pass

class RecommendHandler(Iface):
    def feed(self, req):
        # 得到req中的关键字
        r = redis.Redis(host = "127.0.0.1", port=6379, db=0)
        resources = []
        cnt = random.randint(7,9)
        desc = req.desc
        if len(desc) == 0:
            desc = "我们是工农子弟兵"
        logging.info("desc: %s" % desc)
        c_score = get_c(desc)
        m = dict()
        for c in c_score:
            result = get_dict_by_char(r, c)
            for url in result:
                data = result[url]
                m[url] = data
        mq = list(m.iteritems())
        random.shuffle(mq)
        for i in range(cnt):
            k, d = mq[i]
            title = d['title']
            img = d['img']
            desc = d['desc']
            r = Resource()
            r.cid = 2131
            r.title = title
            r.desc = desc
            r.himg = img
            r.impr = random.randint(1, 10000)
            r.bury = random.random() / 100 * r.impr
            r.digg = random.random() / 100 * r.impr
            r.detail = random.random() / 17 * r.impr
            r.download = random.random() /2 * r.detail
            r.source = k
            resources.append(r)

        rr = RecommendResponse(resource_rsp=resources)
        return rr

    def get_example_resource(self):
        # 测试，返回7个相同的模型
        logging.info(time.time())
        img_path = "http://www.dayinhu.com/data/pic/preview/144/144447.jpg"
        name = u"蜜罐维尼熊"
        r = Resource()
        return r
if __name__ == '__main__':
    get_c("智能装备典型代表是工业机器人，机器人在工业生产中具有很多优点。首先，它们能代替人做某些单调、频繁和重复的长时间作业，或是危险、恶劣环境下的作业。其次，在重复动作中可以保持较高精度，保证产品质量的稳定。第三，机器人可以连续工作，投资回收期较短。最后，机器人的使用成本较低，且便于控制，可以削减昂贵的人工费用，为企业节约大量的成本。")

