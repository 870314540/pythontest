# -*- coding: utf-8 -*
# 百度首页 右上角连接
from urllib2 import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://www.baidu.com')
bd_obj = BeautifulSoup(html.read(),'html.parser')
text_list1 = bd_obj.find_all("a","mnav")   #静态内容
for text in text_list1:
	print(text.get_text().encode("utf8"))   

html.close()


