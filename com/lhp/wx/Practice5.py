# coding: utf-8
# author: S201861548
# 90=2*3*3*5
while True:
    n = int(input('请输入一个整数：'))
    print('{0}='.format(n),end='')
    while n>1:
        for i in range(2,n+1): #range(2,n+1)表示i的取值范围为2~n+1
            if n%i==0:
                n=int(n/i)
                if n==1:
                    print('{}'.format(i),end='')
                else:
                    print('{}*'.format(i),end='')
                break  #跳出for循环
    print()
