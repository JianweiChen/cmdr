# coding=utf8
# 定义CMDR即云制造设计资源的结构
class Cmdr(object):
    """云制造设计资源是一种分布式的、以三维模型为核心的、以简化检索等数据算法为设计目标的编码方式"""
    def __init__(self):
        pass

    def as_byte(self):
        """
        最重要的方法，将一个python的CMDR类转化为字节流的形式，方便传输与redis存储
        :rtype: list of byte
        :return: 
        """
        return []

