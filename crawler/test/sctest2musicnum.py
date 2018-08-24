# -*- coding: utf-8 -*

from selenium import webdriver
import csv
import sys
import defaultcode

print(sys.getdefaultencoding())

path = "/usr/local/bin/chromedriver" # chromedriver完整路径，path是重点
driver = webdriver.Chrome(path)
base_url = 'https://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'

csv_file = open("1.csv","w")
writer = csv.writer(csv_file)
writer.writerow(['title','number','link'])

while base_url != 'javascript:void(0)':
	driver.get(base_url)
	driver.switch_to.frame("contentFrame")
	data = driver.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
	for i in range(len(data)):
		nb = data[i].find_element_by_class_name("nb").text
		if '万' in nb and int(nb.split("万")[0]) > 500 :
			msk = data[i].find_element_by_css_selector("a.msk")
			writer.writerow([msk.get_attribute('title'),nb,msk.get_attribute('href')])
	base_url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')
csv_file.close()