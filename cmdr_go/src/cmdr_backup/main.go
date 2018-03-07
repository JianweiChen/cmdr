package main
import (
	//"git.apache.org/thrift.git/lib/go/thrift"
	//"net"
	//"fmt"
	//"gen-go/cmdr_recommend"
	//"strconv"
	//"context"
	//"encoding/json"
)
import (
	"github.com/astaxie/beego"
	"fmt"
	"git.apache.org/thrift.git/lib/go/thrift"
	"net"
	"gen-go/cmdr_recommend"
	"strconv"
	"context"
	"encoding/json"
	"github.com/astaxie/beego/plugins/cors"
)

type MainController struct {
    beego.Controller
}

func (this *MainController) Get() {
	desc := this.GetString("desc")
	uid := "12"
	var transport thrift.TTransport
	var err error
	transport, err = thrift.NewTSocket(net.JoinHostPort("127.0.0.1", "8291"))
	if err != nil {
		fmt.Println("Error opening socket:", err)
	}
	transportFactory := thrift.NewTTransportFactory()
	protocolFactory := thrift.NewTBinaryProtocolFactoryDefault()
	transport, err = transportFactory.GetTransport(transport)
	if err != nil {
		return
	}
	defer transport.Close()
	if err := transport.Open(); err != nil {
		return
	}
	iprot := protocolFactory.GetProtocol(transport)
	oprot := protocolFactory.GetProtocol(transport)
	client := cmdr_recommend.NewCmdrRecommendClient(thrift.NewTStandardClient(iprot, oprot))
	ctx := context.Background()
	req := cmdr_recommend.NewRecommendRequest()
	req.UID, err = strconv.ParseInt(uid, 10, 64)
	req.Desc = &desc
	rsp, err := client.Feed(ctx, req)
	if err != nil {
		fmt.Print(err.Error())
	}
	j, err := json.Marshal(&rsp)
    this.Ctx.WriteString(string(j))
}

func main() {
	beego.InsertFilter("*", beego.BeforeRouter, cors.Allow(&cors.Options{
        AllowAllOrigins: true,
        AllowMethods:    []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
        AllowHeaders:    []string{"Origin", "Authorization", "Access-Control-Allow-Origin", "Content-Type"},
        ExposeHeaders:   []string{"Content-Length", "Access-Control-Allow-Origin"},
    }))
	beego.Router("/", &MainController{})
	beego.RunWithMiddleWares("0.0.0.0:8888")

}
