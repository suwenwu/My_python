import requests

url = 'https://fanyi.baidu.com/sug'
s = input('请输入你想翻译的单词：\n')
dic = {
    "kw":s
}
resp = requests.post(url, data=dic)
print(resp.json())

resp.close()