# 武汉加油！
这个项目是为了来显示目前实时的疫情情况，特别写的一个小项目。
# 刚刚，地图链接已更改为https://yiqin.zw2s.ltd/guonei这个链接，请务必更新！
~~使用的是Github的Actions作为自动化，实时上传到腾讯云的cos。~~

新版已改为使用腾讯云函数和api网关来实现，之前的已废弃。

目前，新版的API接口已经改为通过腾讯云函数来进行提供，API接口地址如下：
- 国内API：https://api.zw2s.ltd/yiqin/guonei
- 国外API：https://api.zw2s.ltd/yiqin/guowai
- 其他一些数据：https://api.zw2s.ltd/yiqin/data

以上数据来自丁香园，接口均为json格式。

地址：https://yiqin.zw2s.ltd/guonei
# 如何嵌入到网站？
插入以下html代码：
```html
<iframe src="https://yiqin.zw2s.ltd/guonei" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="width:1349px; height:500px;"></iframe>
```
