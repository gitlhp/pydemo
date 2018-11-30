# coding: utf-8
# author: S201861548
def fun(num1, num2):  # 定义一个函数, 两个形参
	if num1 < num2:  # 判读两个整数的大小,目的为了将大的数作为除数,小的作为被除数
		num1, num2 = num2, num1  # 如果if条件满足,则进行值的交换

	vari1 = num1 * num2  # 计算出两个整数的乘积,方便后面计算最小公倍数
	vari2 = num1 % num2  # 对2个整数进行取余数

	while vari2 != 0:  # 判断余数是否为0, 如果不为0,则进入循环
		num1 = num2  # 重新进行赋值,进行下次计算
		num2 = vari2
		vari2 = num1 % num2  # 对重新赋值后的两个整数取余数

	# 直到 vari2 等于0,得到最到公约数就退出循环

	vari1 /= num2  # 得出最小公倍数
	print("最大公约数为:%d" % num2)  # 输出
	print("最小公倍数为:%d" % vari1)  # 输出



if __name__ == '__main__':
	m = int(input("请输入正整数M:"))
	n = int(input("请输入正整数N:"))
	fun(m, n)

