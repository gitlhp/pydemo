# coding: utf-8
# author: S201861548
# 爬取猫眼电影TOP100
import requests
import re
import json
import time

def get_one_page(url):
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36'
	}
	response = requests.get(url,headers=headers)
	if response.status_code == 200:
		return  response.text
	return None

#
# def parse_one_page(html):
# 	pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
# 	items = re.findall(pattern,html)
# 	# print(items)
# 	print(len(items))
# 	for item in items:
# 		index = item[0]
# 		image = item[1]
# 		title = item[2].strip()
# 		actor = item[3].strip()
# 		time = item[4].strip()
# 		score = item[5].strip()+item[6].strip()
# 		print("排名：{0} 图片：{1} 标题：{2} 演员：{3} 上映时间：{4} 评分：{5}".format(index,image,title,actor,time,score))

#
def parse_one_page(html):
	pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
	items = re.findall(pattern,html)
	# print(items)
	# print(len(items))
	for item in items:
		# 迭代返回字典
		yield {
			'index':item[0],
			'image':item[1],
			'title':item[2].strip(),
			'actor':item[3].strip()[3:] if len(item[3])>3 else '',
			'time':item[4].strip()[5:] if len(item[4])>5 else '',
			'score':item[5].strip()+item[6].strip()
		}

# 写入文件
def write_to_file(content):
	with open('result.txt', 'a', encoding='utf-8') as f:
		print(type(json.dumps(content)))
		f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
	url = 'http://maoyan.com/board/4?offset='+str(offset)
	html = get_one_page(url)
	# print(html)
	for item in parse_one_page(html):
		write_to_file(item)

if __name__ == '__main__':
	for i in range(10):
		main(offset=i*10)
		time.sleep(1)



