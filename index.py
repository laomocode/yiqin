from pyecharts.charts import Map
from pyecharts import options as opts
from tencentserverless.scf import Client
from time import strftime,localtime
from requests import get
from json import loads
def main_handler(event, context):
    geo=Map(init_opts=opts.InitOpts(page_title="国内疫情地图",js_host="https://js.yiqin.zw2s.ltd/"))
    scf=Client(secret_id="******",secret_key="******",region="ap-shanghai")
    data=loads(scf.invoke('guonei'))
    data2=loads(scf.invoke('data'))
    updatetime=strftime("%Y-%m-%d %H:%M:%S",localtime(data2['modifyTime']/1000))
    zhongdata=[]
    for a in range(len(data)):
        tempdata=[]
        tempdata.append(data[a]['provinceShortName'])
        tempdata.append(data[a]['currentConfirmedCount'])
        zhongdata.append(tempdata)
    pingjun=data2['currentConfirmedCount']/len(data)
    geo.set_global_opts(title_opts=opts.TitleOpts(title="国内疫情地图",subtitle="目前共确诊"+str(data2['currentConfirmedCount'])+"例，数据来自丁香园，截止时间："+updatetime),visualmap_opts=opts.VisualMapOpts(max_=pingjun),legend_opts=opts.LegendOpts(is_show=False))
    geo.add("确诊",zhongdata, maptype="china")
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html; charset=utf-8'},
        "body": geo.render_embed()
    }