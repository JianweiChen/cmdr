# coding=utf8
# 基于kafka来做这件事情
import json
from collections import defaultdict
from cmdr_recommend import recommend_handler
from tqdm import tqdm
import redis

def pipe_tiger():
    with open("../cmdr_crawler/data.json", 'r') as f:
        for line in (f):
            j = json.loads(line.strip())
            title = j.get('title', "")
            desc = j.get('desc', "")
            cc = recommend_handler.get_c(title)
            cd = recommend_handler.get_c(desc)
            for k in cd:
                cc[k] += cd[k]
            url = j.get('url')
            if not url:
                continue
            value = {
                "title": j.get('title', ""),
                "desc":  j.get('desc', ""),
                "img": j.get("img",""),
                "relates": j.get("relates", []),
                "url": url,
                "source": u"打印虎",
            }
            data = {url: value}
            r = redis.Redis(host="127.0.0.1", port=6379, db=0)
            total = 0
            for c in cc:
                total += cc[c]
            for c in cc:
                mark = cc[c] * 1.0 / total
                data[url]['score'] = mark
                recommend_handler.update_dict_by_char(r, c, data)
            recommend_handler.set_data(r, url, value)
            print(title)






if __name__ == '__main__':

    # r = redis.Redis(host="127.0.0.1", port=6379, db=0)
    # print r.get(u'幽灵')
    pipe_tiger()
