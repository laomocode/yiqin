from pyecharts.charts import Map
from api import api
from pyecharts import options as opts
import os
geo=Map()
api=api()
data=api.guonei()
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
geo.set_global_opts(title_opts=opts.TitleOpts("国内疫情地图"),visualmap_opts=opts.VisualMapOpts(max_=pingjun))
geo.add("确诊",zhongdata, maptype="china")
if os.path.exists('dists')==False:
    os.mkdir('dists')
os.chdir('dists')
geo.render('index.html')