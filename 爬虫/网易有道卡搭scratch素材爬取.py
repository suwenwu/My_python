import requests

#进行数据初始话
for i in range(0,151):
    offset = 30*i #分页的起始
    pageIndex=i   #页码
    relativeOffset = offset  #分页的下一页起始

    url = f'https://kada.163.com/j/search/library/list?limit=30&offset={offset}&pageIndex={pageIndex}&pageSize=30&relativeOffset={relativeOffset}&proType=3&filterType=2&libraryType=0&category=0&filterId=0&st=1'
    resp = requests.get(url)
    dic = resp.json()['result']['list']
    for i in dic:
        if i['libraryUrl'].split('.')[-1] == 'mp3':
            break
        libraryName = i['libraryName'] + '.' + i['libraryUrl'].split('.')[-1]
        libraryUrl = 'http:'+i['libraryUrl']
        try:
            with open('F:/scratch素材/'+libraryName,mode='wb') as f:
                f.write(requests.get(libraryUrl).content)
            print(f'{libraryName}下载完毕')
        except:
            print(f'{libraryName}没有下载下来')
    resp.close()

#访问原始页面

# url = f"https://kada.163.com/j/search/library/list?limit=30&offset=0" \
#       f"&pageIndex=1&pageSize=30&relativeOffset=0&proType=3&filterType=2&libraryType=0&category=0&filterId=0&st=1"
# resp = requests.get(url)
# dic = resp.json()
# #品牌分类
# filterTags = {}
#
#
#
# #获取当前的分类Id和分类名称
# for i in dic['result']['filterTags']:
#     # print(i['id'],i['name'])
#     filterTags[i['id']] =  i['name']
# # print(filterTags)
#
# path = 'F:/scratch素材'
# #开始依次访问每一个品牌分类
# for i in filterTags.keys():
#     offset = 0  # 分页的起始
#     pageIndex = 1  # 页码
#     relativeOffset = 0  # 分页的下一页起始
#     libraryType = 0  # 类型  0代表全部   1代表背景  2代表角色  3代表声音   4代表造型
#     # 类型分类
#     libraryTypeTags = {}
#     filterId = i    # 品牌分类
#     # print(i)
#
#     url = f"https://kada.163.com/j/search/library/list?limit=30&offset={offset}&pageIndex={pageIndex}&pageSize=30&relativeOffset={relativeOffset}&proType=3&filterType=2&libraryType={libraryType}&category=0&filterId={filterId}"
#     print(url)
#     resp_1 = requests.get(url)
#     dic_library = resp.json()
#     print(dic_library)
#     for j in dic['result']['libraryTypeTags']:
#         hitCount = j['hitCount']
#         name = j['name']
#         print(hitCount,name)
#         break
#     path = f'{path}/'+ str(filterTags[i])
#     break
#
#
#
#
#
#
#
#
# resp.close()

