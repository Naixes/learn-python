# coding:utf-8

# Selenium 是 Web 应用的测试工具，可以直接运行在浏览器中，它的原理是模拟用户在进行操作，支持当前多种主流的浏览器。

# 运行失败???

# pip安装库：pip install selenium，安装报错
# 手动安装：下载压缩包https://pypi.org/project/selenium/#files解压到python安装路径，安装：python xxx.py install

# 配置chromedriver：http://chromedriver.storage.googleapis.com/index.html下载对应版本的exe放在Chrome的根目录下
# 配置环境变量：在path路径下添加文件所在的根目录。比如：C:\Program Files (x86)\Google\Chrome\Application

from selenium import webdriver
import requests
from lxml import etree

# 下载图片
def downloadImage(src, id):
        print(src)
        print(id)
        dir = './' + str(id) + '.jpj'
        print(dir)
        try:
                pic = requests.get(src, timeout=10)
                
                fp = open(dir, 'wb')
                fp.write(pic.content)
                fp.close()
        except requests.exceptions.ConnectionError:
    	        print('图片无法下载')

request_url = "https://www.douban.com/search?cat=1002&q=%E7%8E%8B%E7%A5%96%E8%B4%A4"
src_xpath = "//div[@class='result']/div[@class='pic']/a[@class='nbg']/img/@src"
title_path = "//div[@class='title']/h3/a"

# 通过 WebDriver 创建一个 Chrome 浏览器的 drive，再通过 drive 获取访问页面的完整 HTML。
driver = webdriver.Chrome()
driver.get(request_url)

html = requests.get(request_url).text
html = etree.HTML(html)

# response = requests.get(request_url).text
# html = json.loads(response, encoding='utf-8')

srcs = html.xpath(src_xpath)
titles = html.xpath(title_path)

# 循环下载
for src, title in zip(srcs, titles):
        downloadImage(src, title.text)

