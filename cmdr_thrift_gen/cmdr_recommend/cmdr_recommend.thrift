# Thrift for CMDR ( Cloud Manufacturing Design Resources)
# Mode
enum ModeType {
    RESOURCE_MODE =     0x01,    # 资源检索，也是最主要的功能
    DEMAND_MODE =   0x02,    # 需求检索，用来有针对性的帮助别人
    SITE_MODE = 0x04,    # 站点检索，寻找某个站点是否在cmdr的索引中
    USER_MODE = 0x08
    UPLOAD_MODE = 0x10, # 上传资源时的去重检索，比普通的资源检索更有针对性
}
# Sign
enum SignType {
    FEED_SIGN = 0x01,   # 下拉，推荐新的资源
    BACK_SIGN = 0x02,   # 下拉，加载之前看过的资源
    PASSIVE_SIGN = 0x04,    # 被动检索，比如上传草图之后
}

struct RecommendRequest {
    1: required i64 uid,    # 用户id
    2: optional ModeType mode,  # 检索模式
    3: optional SignType sign,

    4: optional string desc, # 描述，可以为空
    # 其他内容将来再加，先实现完全基于用户和文字query的功能
}

struct Resource {
    1: required i64 cid, # cmdr的id
    2: optional string title,
    3: optional string desc,
    4: optional string himg, # 封面图片
    5: optional string source, # 来源站点
    6: optional i32 digg,
    7: optional i32 bury,
    8: optional i32 impr,
    9: optional i32 detail,
    10: optional i32 download,
    # 命中的关键词一定要返回，这是可解释性的来源，当然这个关键词
    # 命中的草图 也是required，就算没有合适的草图，也要弄一个
}

struct RecommendResponse {
    1: required list<Resource> resource_rsp
}

struct Demand {
    1: required i64 did, # demand的id，需求id
}

service CmdrRecommend {
    RecommendResponse feed(1:RecommendRequest req)
}