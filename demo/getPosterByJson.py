# coding:utf-8

# Requests 是 Python HTTP 的客户端库

# r.text 或 r.content 可以来获取HTML 的正文。
# r = requests.get('http://www.douban.com')

# post
# data 的数据类型是个字典的结构，采用 key 和 value 的方式进行存储。

# r = requests.post('http://xxx.com', data = {'key':'value'})
# https://github.com/psf/requests下载解压到python安装路径，安装：python xxx.py install


''' 使用json数据格式下载豆瓣王祖贤图片'''

# 引入requestshejson
import requests
import json

query = '王祖贤'

# 函数必须先声明后使用
# 下载图片
def downloadImage(src, id):
        dir = './' + str(id) + '.jpg'
        try:
                pic = requests.get(src, timeout=10)
                
                # 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
                fp = open(dir, 'wb')
                fp.write(pic.content)
                fp.close()
        except requests.exceptions.ConnectionError:
    	        print('图片无法下载')

# 循环请求url
for i in range(0, 20, 20):
        url = 'https://www.douban.com/j/search_photo?q='+query+'&limit=20&start='+str(i)

        # 请求url：r.text 或 r.content 可以来获取 HTML（接口） 的正文
        response = requests.get(url).text
        # print(response)

        # json转换为python对象
        result = json.loads(response, encoding='utf-8')

        # 循环下载图片
        for image in result['images']:
                # 查看当前下载的图片网址
                print(image['src']) 
                # 下载一张图片
                downloadImage(image['src'], image['id'])
