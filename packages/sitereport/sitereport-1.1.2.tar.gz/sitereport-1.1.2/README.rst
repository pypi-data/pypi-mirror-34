siteReport Api
=================

https://www.sitereport.cn  接口SDK

支持 py2,py3


安装
======
pip install sitereport


使用
======

import sitereport

access_key=""

access_secret=""

api=sitereport.Api(access_key,access_secret)

查询360收录

status,result=api.request("/360/count",{'q':'site:www.taobao.com'})

print(result)

与可以

status,result=api.haosou_count({'q':'site:www.taobao.com'})

print(result)

更多接口用法请到官网查看
