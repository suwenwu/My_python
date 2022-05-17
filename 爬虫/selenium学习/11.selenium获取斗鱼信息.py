import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class DouYu(object):
    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.web = Chrome()
        self.web.implicitly_wait(5)

    def get_data(self):
        room_list = self.web.find_elements(By.XPATH, '//*[@id="listAll"]/section[2]/div[2]/ul/li')
        room_info = []
        for room in room_list:
            info = {}
            info['title'] = room.find_element(By.XPATH, './div/a/div[2]/div[1]/h3').text
            info['zone'] = room.find_element(By.XPATH, './div/a/div[2]/div[1]/span').text
            info['user'] = room.find_element(By.XPATH, './div/a/div[2]/div[2]/h2').text
            info['hot'] = room.find_element(By.XPATH, './div/a/div[2]/div[2]/span').text
            room_info.append(info)
        return room_info

    def save_info(self, room_info):
        for info in room_info:
            print(info)

    def run(self):
        self.web.get(self.url)
        time.sleep(2)
        while True:
            # 获取房间信息
            room_info = self.get_data()
            # 打印信息
            self.save_info(room_info)
            # 翻页
            try:
                next = self.web.find_element(By.XPATH, '//li[@class=" dy-Pagination-next"]')
                self.web.execute_script('window.scrollTo(0,100000)')
                next.click()
                time.sleep(1)
            except:
                break


if __name__ == '__main__':
    douyu = DouYu()
    douyu.run()
