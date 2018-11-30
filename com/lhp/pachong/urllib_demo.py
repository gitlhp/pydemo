# coding: utf-8
# author: S201861548

# import  urllib
#
# def print_list(list):
# 	for x in list:
# 		print(x)
#
# def demo():
# 	url=urllib.urlopen('http://www.baidu.com')
# 	msg = url.info()
# 	print_list(msg)
#
# def retrieve():
# 	urllib.urlretrieve('http://www.baidu.com','lhp1.html')
#
# if __name__ == '__main__':
# 	# demo()
#     retrieve()

# from urllib import request
#
# if __name__ == "__main__":
#     req = request.Request("http://fanyi.baidu.com/")
#     response = request.urlopen(req)
#     html = response.read()
#     html = html.decode("utf-8")
#     print(html)


# from urllib import request
# import chardet
#
# if __name__ == "__main__":
#     response = request.urlopen("http://fanyi.baidu.com/")
#     html = response.read()
#     charset = chardet.detect(html)
#     print(charset)
# print(html)


# from urllib import request
from urllib import request
#
# if __name__ == "__main__":
# 	# 返回一个URL对象
#     req = request.Request("http://fanyi.baidu.com/")
#     response = request.urlopen(req)
#     html = response.read()
#     html = html.decode("utf-8")
#     print(html)


# Test
# from urllib import request
#
# if __name__ == "__main__":
#     req = request.Request("http://fanyi.baidu.com/")
#     response = request.urlopen(req)
#     print("geturl打印信息：%s"%(response.geturl()))
#     print('**********************************************')
#     print("info打印信息：%s"%(response.info()))
#     print('**********************************************')
#     print("getcode打印ss信息：{0}".format(response.getcode()))

# test2有道翻译
# from urllib import request
# from urllib import parse
# import json
#
# if __name__ == "__main__":
#     #对应上图的Request URL
#     Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
#     #创建Form_Data字典，存储上图的Form Data
#     Form_Data = {}
#     Form_Data['type'] = 'AUTO'
#     Form_Data['i'] = 'Jack'
#     Form_Data['doctype'] = 'json'
#     Form_Data['xmlVersion'] = '1.8'
#     Form_Data['keyfrom'] = 'fanyi.web'
#     Form_Data['ue'] = 'ue:UTF-8'
#     Form_Data['action'] = 'FY_BY_CLICKBUTTON'
#     #使用urlencode方法转换标准格式
#     data = parse.urlencode(Form_Data).encode('utf-8')
#     #传递Request对象和转换完格式的数据
#     response = request.urlopen(Request_URL,data)
#     #读取信息并解码
#     html = response.read().decode('utf-8')
#     #使用JSON
#     translate_results = json.loads(html)
#     #找到翻译结果
#     translate_results = translate_results['translateResult'][0][0]['tgt']
#     #打印翻译信息
#     print("翻译的结果是：%s" % translate_results)


# test有道翻译改编版   在线翻译
from urllib import request
from urllib import parse
import json

if __name__ == "__main__":
	# 对应上图的Request URL
	request_url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
	while True:
		content = input("请输入你想要翻译的内容：")
		# 创建Form Data字典，存储上图中的Form Data
		Form_Data = {}
		Form_Data['i'] = content
		Form_Data['from'] = 'AUTO'
		Form_Data['to'] = 'AUTO'
		Form_Data['smartresult'] = 'dict'
		Form_Data['client'] = 'fanyideskweb'
		Form_Data['doctype'] = 'json'
		Form_Data['version'] = '2.1'
		Form_Data['keyfrom'] = 'fanyi.web'
		Form_Data['action'] = 'FY_BY_REALTIME'
		Form_Data['typoResult'] = 'false'
		# 使用urlencode方法转换标准格式  py2参数只能是字典类型
		data = parse.urlencode(Form_Data).encode('utf-8')
		# 传递Request对象和转换完格式的数据
		response = request.urlopen(request_url, data)
		# 读取信息并解码  Json对象 返回的网页内容实际上是没有被解码
		html = response.read().decode('utf-8')
		# 使用json  转化为字典对象
		translate_results = json.loads(html)
		# 找到翻译结果
		translate_result = translate_results["translateResult"][0][0]['tgt']
		# 打印翻译结果
		print("翻译的结果是 ：{}".format(translate_result))

# 异常处理
# from urllib import request
# from urllib import error
#
# if __name__ == "__main__":
#     #一个不存在的连接
#     url = "http://www.douyu.com/Jack_Cui.htmld"
#     req = request.Request(url)
#     try:
#         responese = request.urlopen(req)
#         # html = responese.read()
#     except error.HTTPError as e:
#         print(e.code)


# 异常处理2
# from urllib import request
# from urllib import error
#
# if __name__ == "__main__":
#     #一个不存在的连接
#     url = "http://www.douyu.com/Jack_Cui.html"
#     req = request.Request(url)
#     try:
#         responese = request.urlopen(req)
#     except error.URLError as e:
#         if hasattr(e, 'code')
#             print("HTTPError")
#             print(e.code)
#         elif hasattr(e, 'reason')
#             print("URLError")
#             print(e.reason)
