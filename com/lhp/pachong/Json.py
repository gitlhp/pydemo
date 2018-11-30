# coding: utf-8
# author: S201861548
#读取json数据
# import json
#
# str='''
# [{
# "name":"bob",
# "gender":"male",
# "birthday":"1992-10-18"
# },
# {"name":"bob1",
# "gender":"male2",
# "birthday":"1993-10-18"
# }]
# '''
# print(type(str))
# data = json.loads(str)
# print(data)
# print(type(data))

# 将json对象转换为字符串
import json

data = [{
	'name':'lhp',
	'age':22,
	'sex':'x'
}]
data1={
	"ss":2
}

print(type(data))
print(type(data1))

json = json.dumps(data)
print(data)

with open('data.json','w') as file:
	file.write(json)