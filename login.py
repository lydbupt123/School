import http.client
import urllib

url="http://10.3.8.211//"

reqheaders={
    'Host': '10.3.8.211',
    'Connection': 'keep-alive',
    'Content-Length': '37',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://10.3.8.211',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://10.3.8.211/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'myusername=2016110775; username=2016110775; smartdot=081837'
    }

pdata={
    'DDDDD':'2016110775',
    'upass':'081837',
    '0MKKey':None
    }

data=urllib.parse.urlencode(pdata)
conn=http.client.HTTPConnection('10.3.8.211')
conn.request('POST','',data,reqheaders)

res=conn.getresponse()

print(res.status)
print(res.msg)
print(res.getheader('Set-Cookie'))



