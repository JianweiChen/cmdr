# coding=utf8
# 掠夺者要塞
class StrongHold(object):
    """掠夺者要塞主要是对一个站点的抓取情况进行管理，每个站点只在一个要塞中维护，每个物理机器只起一个要塞\n
    掠夺者包含一个thrift的client接口，会调取要塞的现状服务，并传回自己所掌握的"情报"供要塞分析
    """
    def __init__(self):
        pass

