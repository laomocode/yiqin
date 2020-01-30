from pyecharts.charts import Map
from api import api
from pyecharts import options as opts
import os
import time
geo=Map()
api=api()
data=api.guonei()
data2=api.data()
updatetime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(data2['modifyTime']/1000))
zhongdata=[]
deaddata=[]
zhiyu=[]
for a in range(len(data)):
    tempdata=[]
    tempdeaddata=[]
    tempzhiyu=[]
    tempdata.append(data[a]['provinceShortName'])
    tempdata.append(data[a]['confirmedCount'])
    tempdeaddata.append(data[a]['provinceShortName'])
    tempdeaddata.append(data[a]['deadCount'])
    tempzhiyu.append(data[a]['provinceShortName'])
    tempzhiyu.append(data[a]['curedCount'])
    zhongdata.append(tempdata)
    deaddata.append(tempdeaddata)
    zhiyu.append(tempzhiyu)
pingjun=(data2['confirmedCount']+data2['deadCount']+data2['curedCount'])/len(data)
geo.set_global_opts(title_opts=opts.TitleOpts(title="国内疫情地图",subtitle="数据来自丁香园，截止时间："+updatetime),visualmap_opts=opts.VisualMapOpts(max_=pingjun))
geo.add("确诊",zhongdata, maptype="china")
geo.add("死亡",deaddata,maptype="china")
geo.add("治愈",zhiyu,maptype="china")
if os.path.exists('dists')==False:
    os.mkdir('dists')
os.chdir('dists')
geo.render('index.html')