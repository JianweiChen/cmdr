# coding=utf8
# 数据主服务

from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport, TSocket
from thrift.server import TServer
from cmdr_recommend.recommend_handler import RecommendHandler
from cmdr_recommend.idl.cmdr_recommend.CmdrRecommend import Processor

handler = RecommendHandler()
processor = Processor(handler)
transport = TSocket.TServerSocket(host="127.0.0.1", port=8291)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
server.daemon = True
server.serve()



