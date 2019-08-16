# Requests 是 Python HTTP 的客户端库


# r.text 或 r.content 可以来获取HTML 的正文。
# r = requests.get('http://www.douban.com')

# post
# data 的数据类型是个字典的结构，采用 key 和 value 的方式进行存储。
# r = requests.post('http://xxx.com', data = {'key':'value'})

# coding:utf-8
# https://github.com/psf/requests下载解压到python安装路径，安装：python xxx.py install
import requests
import json
query = '王祖贤'
''' 下载图片 '''
def download(src, id):
    dir = './' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
    	print('图片无法下载')
''' for 循环 请求全部的 url '''
for i in range(0, 22471, 20):
    url = 'https://www.douban.com/j/search_photo?q='+query+'&limit=20&start='+str(i)
    html = requests.get(url).text # 得到返回结果
    response = json.loads(html,encoding='utf-8') # 将 JSON 格式转换成 Python 对象
    for image in response['images']:
        print(image['src']) # 查看当前下载的图片网址
        download(image['src'], image['id']) # 下载一张图片

