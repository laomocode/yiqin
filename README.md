# 武汉加油！
这个项目是为了来显示目前实时的疫情情况，特别写的一个小项目。

~~使用的是Github的Actions作为自动化，实时上传到腾讯云的cos。~~

新版已改为使用腾讯云函数和api网关来实现，之前的已废弃。

目前，新版的API接口已经改为通过腾讯云函数来进行提供，API接口地址如下：
- 国内API：https://api.yiqin.zw2s.ltd/guonei
- 国外API：https://api.yiqin.zw2s.ltd/guowai
- 其他一些数据：https://api.yiqin.zw2s.ltd/data

以上数据来自丁香园，接口均为json格式。

地址：https://yiqin.zw2s.ltd