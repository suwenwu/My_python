import re
str = r'\d+'
# ret = re.finditer(str,'我的电话号码：11010，我朋友的电话号码：10086')
# for i in ret:
#     print(i.group())

ret2 = re.search(str,'我的电话号码：11010，我朋友的电话号码：10086')
print(ret2.group())
