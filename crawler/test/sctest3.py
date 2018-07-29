# -*- coding: utf-8 -*
# 百度首页 右上角连接
# from urllib2 import urlopen

# from bs4 import BeautifulSoup

# html = urlopen('http://www.baidu.com')
# bd_obj = BeautifulSoup(html.read(),'html.parser')
# text_list1 = bd_obj.find_all("a","mnav")   #静态内容
# for text in text_list1:
# 	print(text.get_text().encode("utf8"))   

# html.close()


from selenium import webdriver
path = "/usr/local/bin/chromedriver" # chromedriver完整路径，path是重点
driver = webdriver.Chrome(path)
base_url = 'https://www.baidu.com'
driver.get(base_url)  #驱动打开网址

# options=webdriver.ChromeOptions()
# options.set_headless()
# # options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# driver=webdriver.Chrome(options=options)
# driver.get('http://httpbin.org/user-agent')
# driver.get_screenshot_as_file('test.png')
# driver.close()

