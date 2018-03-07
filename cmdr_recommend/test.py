# coding=utf8

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from cmdr_recommend.idl.cmdr_recommend.CmdrRecommend import Client
from cmdr_recommend.idl.cmdr_recommend.ttypes import RecommendResponse, RecommendRequest

transport = TSocket.TSocket(host="localhost", port=8291)
transport = TTransport.TBufferedTransport(transport)
protocal = TBinaryProtocol.TBinaryProtocol(transport)
client = Client(protocal)
transport.open()
req = RecommendRequest(uid=12)
rsp = client.feed(req)
print(rsp)
