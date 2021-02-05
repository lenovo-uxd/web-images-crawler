import requests
import time
import os
from bs4 import BeautifulSoup
import urllib.request
import zipfile
import urllib.parse

os.makedirs('./images/', exist_ok=True)

def download_url(url, save_path):
	req = urllib.request.Request(url, headers={"User-Agent": "Chrome"})
	with urllib.request.urlopen(req) as dl_file:
		with open(save_path, 'wb') as out_file:
			out_file.write(dl_file.read())

#翻页的页数设置
for i in range(14,58):
	#需要爬的网站的链接
	url = "https://www.toptal.com/designers/subtlepatterns/page/"+str(i)
	#请求链接返回页面html
	strhtml = requests.get(url)
	#解析为lxml
	soup = BeautifulSoup(strhtml.text,'lxml')
	#css选择器选择下载链接节点
	downloadLinks = soup.select('.download')

	#存储链接内容
	for urllink in downloadLinks:
		#延时1秒防止被封
		time.sleep(1)
		#下载链接
		link = urllib.parse.quote(urllink["href"])

		print(link)

		if link.find("https://www.toptal.com")<0:
			link = "https://www.toptal.com"+link

		if link.find(".zip")<0:
			print("bad link")
			continue

			
		urlList = urllink["href"].split("/")
		#文件名
		name = urlList[len(urlList)-1]
		download_url(link, './images/'+name)

