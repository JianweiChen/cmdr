# coding=utf8
# 掠夺者
"""掠夺者的输出是stl文件与html链，每个pipeline进程只用于处理本机上掠夺者sacker产生的资料\n每隔一段时间，掠夺者产生的资料会被清空\n
掠夺者产生的大数据如stl文件会存在本机/var/stl/文件夹下，如果将来有其他资源也可以起别的文件夹
比较小的数据打进kafka，毕竟这个东西存着没用，必须被下游消费了才有价值
"""
import requests

class Sacker:
    """掠夺者用来在其他站点寻找云制造设计资源，sacker之间需要交互防止取重了（只是位置上的，内容上的去重不在这里做）
    必然要定义抓取并拼接.stl路径的规则
    """
    def run(self):
        pass

class LinearScaker(Sacker):
    name = "" # 网站的名字，比如说魔猴网


class Drama(object):
    """剧本类
    制造业资源中3D打印模型相关的网站的结构都非常的简单
    一般是一个列表，然后
    """
    img_list_flag = False # 如果是真，图像从列表页中抓取
    url = 'div.cc//a.div$href' # 列表页中的链接网址
    title = "div.title" # 题目
    descs = [] # 网页中的其他文本
    img = "img.img" # 网页中的

