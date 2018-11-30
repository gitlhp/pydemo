# coding: utf-8
# author: S201861548
# import math
# #
# # for i in range(100, 1000):
# # 	x = math.floor(i / 100)  # 获得百位数
# # 	y = math.floor((i - x * 100) / 10)  # 获得十位数
# # 	z = i - math.floor(i / 10) * 10  # 获得个位数
# # 	if i == x ** 3 + y ** 3 + z ** 3:
# # 		print(i,end=',')
# # 		# print("水仙花数有：",i)

tmpStr = input('请输入字符串：')
alphaNum=0
numbers=0
spaceNum=0
otherNum=0
for i in tmpStr:
    if i.isalpha():
        alphaNum +=1
    elif i.isnumeric():
        numbers +=1
    elif i.isspace():
        spaceNum +=1
    else:
        otherNum +=1
print('字母=%d'%alphaNum)
print('数字=%d'%numbers)
print('空格=%d'%spaceNum)
print('其他=%d'%otherNum)
