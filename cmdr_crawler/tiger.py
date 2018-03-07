# coding=utf8
# 抓打印虎的模型

import requests
from lxml import html
import json
import time
import tqdm


def download_page(n, f):
    url = "http://www.dayinhu.com/list/latest?page=%d" % n
    r = requests.get(url)
    dom = html.fromstring(r.text)
    # 得到所有的detai的url
    ys = dom.xpath('//div[@class="listimgdiv"]/a')
    zs = dom.xpath('//div[@class="listimgdiv"]/a/img')
    yzs = zip(ys, zs)
    for y in yzs:
        download_item(y[0].get('href') or "-", y[1].get('src') or "#", f)


def download_item(url, img, f):
    if url == "-":
        return
    t = requests.get(url).text
    dom = html.fromstring(t)
    # 面包屑
    breads = dom.xpath('//span[@class="bc"]')
    if not breads:
        breads = []
    bread = " ".join([b.text or "-" for b in breads])
    # 题目
    titles = dom.xpath('//h2[@class="title"]')
    if not titles:
        titles = []
    title = " ".join([b.text or "-" for b in titles])
    # 图片
    img = img
    # 描述
    descs = dom.xpath('//div[@class="col-md-4"]/p')
    if not descs:
        descs =[]
    desc = " ".join([b.text  or "-" for b in descs])
    # 评分
    infos = dom.xpath('//div[@class="col-md-8 col-sm-8 col-xs-8 info-content"]')
    if not infos:
        infos = []
    info = " ".join([b.text or "-" for b in infos])
    # 相关
    relates = dom.xpath('//div[@class="col-md-2"]/a')
    if not relates:
        relates = []
    relates = [b.get('href') or "-" for b in relates]
    j = {
        'title': title,
        'url': url,
        'img': img,
        'info': info,
        'relates': relates,
        "desc": desc
    }
    value = json.dumps(j)
    print >> f, value
if __name__ == '__main__':
    with open("./data.json", 'w') as f:
        for i in tqdm.tqdm(range(3, 3304)):
            download_page(i, f)
