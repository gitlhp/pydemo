# coding: utf-8
# author: S201861548
# from urllib import request
# from urllib import parse
# import json
#
# def fanyi(input_file,output_file):
# 	# 对应上图的Request URL
# 	request_url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
# 	# 创建Form Data字典，存储上图中的Form Data
# 	file=open(input_file)
# 	content=file.read()
# 	file.close()
# 	Form_Data = {}
# 	Form_Data['i'] = content
# 	Form_Data['from'] = 'AUTO'
# 	Form_Data['to'] = 'AUTO'
# 	Form_Data['smartresult'] = 'dict'
# 	Form_Data['client'] = 'fanyideskweb'
# 	Form_Data['doctype'] = 'json'
# 	Form_Data['version'] = '2.1'
# 	Form_Data['keyfrom'] = 'fanyi.web'
# 	Form_Data['action'] = 'FY_BY_REALTIME'
# 	Form_Data['typoResult'] = 'false'
# 	# 使用urlencode方法转换标准格式  py2参数只能是字典类型
# 	data = parse.urlencode(Form_Data).encode('utf-8')
# 	# 传递Request对象和转换完格式的数据
# 	response = request.urlopen(request_url, data)
# 	# 读取信息并解码  Json对象 返回的网页内容实际上是没有被解码
# 	html = response.read().decode('utf-8')
# 	# 使用json  转化为字典对象
# 	translate_results = json.loads(html)
# 	# 找到翻译结果
# 	translate_result = translate_results["translateResult"][0][0]['tgt']
# 	# 打印翻译结果
# 	print("翻译的结果是 ：{}".format(translate_result))
# 	output=open(output_file,'w')
#
# 	output.write(translate_result)
# 	output.close()
#
#
#
#
# if __name__ == "__main__":
# 	input_file=input("请输入你所要翻译的文件地址：")
# 	output_file='H:\outputfanyi.txt'
# 	fanyi(input_file,output_file)
from  numpy import *
random.rand(4,4)