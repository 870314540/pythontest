# -*- coding: utf-8 -*

from selenium import webdriver
import csv
import sys
import defaultcode

print(sys.getdefaultencoding())

path = "/usr/local/bin/chromedriver" # chromedriver完整路径，path是重点
driver = webdriver.Chrome(path)
base_url = 'https://music.163.com/#/discover/toplist'
driver.get(base_url)
driver.switch_to.frame("contentFrame")

data = driver.find_element_by_id("toplist")

print(data.find_element_by_class_name("s-fc6").text)

data = driver.find_element_by_id("play-count")
print(data.text)


# csv_file = open("1.csv","w")
# writer = csv.writer(csv_file)
# writer.writerow(['title','time','singer'])
# driver.get(base_url)
 

# writer.writerow(['总数:',])

	
# 	data = driver.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
# 	for i in range(len(data)):
# 		nb = data[i].find_element_by_class_name("nb").text
# 		if '万' in nb and int(nb.split("万")[0]) > 500 :
# 			msk = data[i].find_element_by_css_selector("a.msk")
# 			writer.writerow([msk.get_attribute('title'),nb,msk.get_attribute('href')])


# csv_file.close()