from pyecharts.charts import Map
from api import api
from pyecharts import options as opts
import os
import time
geo=Map()
api=api()
data=api.guonei()
data2=api.data()
updatetime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(data2['modifyTime']/1000+28800))
zhongdata=[]
pingjundata=[]
sum=0
for a in range(len(data)):
    tempdata=[]
    tempdata.append(data[a]['provinceShortName'])
    tempdata.append(data[a]['confirmedCount'])
    pingjundata.append(data[a]['confirmedCount'])
    zhongdata.append(tempdata)
for a in range(len(pingjundata)):
    sum=sum+pingjundata[a]
pingjun=sum/len(pingjundata)
geo.set_global_opts(title_opts=opts.TitleOpts(title="国内疫情地图",subtitle="数据来自丁香园，截止时间："+updatetime),visualmap_opts=opts.VisualMapOpts(max_=pingjun))
geo.add("确诊",zhongdata, maptype="china")
if os.path.exists('dists')==False:
    os.mkdir('dists')
os.chdir('dists')
geo.render('index.html')