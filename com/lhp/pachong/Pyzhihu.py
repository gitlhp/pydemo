# coding: utf-8
# author: S201861548
# 爬取知乎热门话题保存在txt文件中

import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36'
}
html = requests.get(url,headers=headers).text
doc=pq(html)
items=doc('.explore-tab .feed-item').items()
for item in items:
	question = item.find('h2').text()
	author = item.find('.author-link-line').text()
	answer = pq(item.find('.content').html()).text()
	# ‘a’追加，一种文件打开方式 以便下次写入的时候直接从文本末尾进行写入  open()获取一个操作该文件的对象
	file = open('explore.text','a',encoding='utf-8')
	# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串（下边语句是用+分割列表元素）
	file.write('\n'.join([question,author,answer]))
	# ===========分隔符
	file.write('\n'+'='*50+'\n')
	file.close()
# with open('') as file 不需要关闭文件资源