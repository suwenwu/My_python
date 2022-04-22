import re
import requests
# 忽略requests证书警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

domain =  "https://www.dytt89.com/"
#verify = False,去掉安全验证
resp = requests.get(domain,verify=False)
resp.encoding = 'gb2312'
#print(resp.text)


obj1 = re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"<a href='/(?P<href>.*?)'",re.S)
obj3 = re.compile(r"片　　名　(?P<movie>.*?)<br />.*?<td "
                  r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []

for i in result1:
    ul = i.group('ul')
    #提取ul内的href标签
    result2 = obj2.finditer(ul)
    for j in result2:
        #拼接子页面url
        child_href = domain + j.group('href')
        child_href_list.append(child_href)

#提取子页面内容
for herf in child_href_list:
    child_resp = requests.get(herf,verify=False)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    # print(result3)
    print(result3.group('movie'))
    print(result3.group('download'))
    child_resp.close()

resp.close()
