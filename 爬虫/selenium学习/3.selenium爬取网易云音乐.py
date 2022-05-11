from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from lxml import etree
import requests

web = webdriver.Chrome()

web.get('https://music.163.com/#/discover/toplist')

time.sleep(1)
# 进入iframe
iframe = web.find_element(By.ID, 'g_iframe')
web.switch_to.frame(iframe)
page_text = web.execute_script('return document.documentElement.outerHTML')

page = etree.HTML(page_text)

trs = page.xpath('//tr')
id_list = []
song_name_list = []
singer_list = []

for tr in trs[1:]:
    music_id = tr.xpath("./td[2]/div[1]/div[1]/span/@data-res-id")[0]  #
    id_list.append(music_id)
    song_name = tr.xpath("./td[2]/div/div/div/span/a/b/@title")[0]
    song_name_list.append(song_name)
    # print(music_id, "----", song_name)

url = 'https://link.hhtjim.com/163/{}.mp3'
try:
    for song_id in id_list:
        my_index = id_list.index(song_id)
        song_name = song_name_list[my_index]
        resp = requests.get(url.format(song_id))
        with open('E:/音乐/music/' + song_name + '.mp3', mode='wb') as f:
            f.write(resp.content)
            print('歌曲:%s下载成功' % song_name)
        resp.close()
except Exception as error:
    print(error)
