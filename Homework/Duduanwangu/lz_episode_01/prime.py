# 1����100w�ڵ�����
# �ж����ݣ���������n�������2������n֮�����������ȥ����
# ���޷���������nΪ����

from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for n in range(1, 1000001):
    is_prime(n)
    if is_prime(n) == True:
        print(n, end=" ")
