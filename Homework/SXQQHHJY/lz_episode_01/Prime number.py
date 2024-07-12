def f(n):    #定义一个函数用来判断一个数是否是质数
    A = range(2,n)    #质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数
    b = 0
    for a in A:    #创建一个循环判断是否有其它因数
        if n % a == 0:
            b = b + 1
    if b == 0:
        return n    #
for c in range(3,1000000):  #判断100万以内的质数
    if f(c) == c:
        print(c)    #输出结果