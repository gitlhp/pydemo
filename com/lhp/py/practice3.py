# coding: utf-8
# author: S201861548
# python 平方根
# num = input("请输入一个数字：")
# num1 = float(num)
#
#
# num_sqrt = num1 ** 0.5
# # print(' %0.3f 的平方根为 %0.3f'%(num1 ,num_sqrt))
# print(' {0} 的平方根为 {1}'.format(num1,num_sqrt))

#
# import random
# print(random.randint(0,9))

# lower=int(input("请输入区间的最小值："))
# upper=int(input("请输入区间的最大值："))
#
# for num in range(lower,upper+1):
# 	# 素数大于1
# 	if num > 1:
# 		for i in range(2,num):
# 			if(num % i==0):
# 				break
# 		else:
# 			print(num)

# x=10
# y=20
# x,y=y,x
# print(x)
# print(y)

# num = float(input("输入一个数字："))
# if num >=0:
# 	if num ==0:
# 		print("==0")
# 	else:
# 		print("+++")
# else:
# 	print("---")

# while True:
# 	try:
# 		num=float(input("请输入一个数字："))
# 		if num == 0:
# 			print('输入的数字是零')
# 		elif num > 0:
# 			print('输入的数字是正数')
# 		else:
# 			print('输入的数字是负数')
# 		break
# 	except ValueError:
# 		print('输入无效，需要输入一个数字')

# 定义一个函数
# def hcf(x, y):
# 	"""该函数返回两个数的最大公约数"""
#
# 	# 获取最小值
# 	smaller=min(x,y)
#
#
# 	for i in range(1, smaller + 1):
# 		if ((x % i == 0) and (y % i == 0)):
# 			hcf = i
#
# 	return hcf
#
#
# # 用户输入两个数字
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
#
# print(num1, "和", num2, "的最大公约数为", hcf(num1, num2))


# 斐波那契数列
# def fibo(n):
# 	if n <= 1:
# 		return  n
# 	else:
# 		return (fibo(n-1)+fibo(n-2))
#
#
# try:
# 	n = int(input("你想输出几项？："))
# 	if n <= 0:
# 		print("请输入正数")
# 	else:
# 		print("数列为：")
# 		for i in range(n):
# 			print(fibo(i))
# except ValueError:
# 	print('输入无效，需要输入一个数字')

# 文件IO
# with open("H:\input_assign04_03.dat.txt","wt") as out_file:
# 	out_file.write("都是大V深Vv")
#
# with open("H:\input_assign04_03.dat.txt","rt") as in_file:
# 	text = in_file.read()
#
# print(text)
#
# li=[1,9,8,4]
# li1=[a*2 for a in li]
# print(li)
# print(li1)
