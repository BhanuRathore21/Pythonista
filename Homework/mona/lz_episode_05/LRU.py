import time
import pickle  # ���������л�
import hashlib  # �õ����л����ݺ���ַ���
import functools  # ����ԭ����������


class Node:  # ����LRU����������һ������
    def __init__(self, key, value, time, pre=None, nxt=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.nxt = nxt
        self.time = time


def judge_time(entryTime, expire_date):
    d = time.time() - entryTime
    return d > expire_date


def hash_key(funcName, args, kwargs):
    key = pickle.dumps((funcName, args, kwargs))
    return hashlib.md5(key).hexdigest()


class Cache:
    def __init__(self, expire_date=3):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None, pre=self.head)
        self.head.nxt = self.tail
        self.expire_date = 3

    def __call__(self, func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            key = hash_key(func.__name__, args, kwargs)  # �õ���״̬��hashֵ���ж��Ƿ�����

            t = self.head.nxt
            while t is not self.tail:  # �жϲ����
                if t.key == key:
                    if not judge_time(t.time, self.expire_date):  # ����������У����Ѹýڵ������ǰ��
                        print('Hey! You have just calculated it!', end=' --> ')
                        t.nxt.pre = t.pre
                        t.pre.nxt = t.nxt
                        self.head.nxt.pre = t
                        t.nxt = self.head.nxt
                        self.head.nxt = t
                        t.pre = self.head
                        return t.value
                    else:  # ��ʱ�˾Ͱ�����Ϊû��ָ��ָ�����Ľڵ㣬��python�Զ����տռ�
                        t.pre.nxt = t.nxt
                        t.nxt.pre = t.pre
                        break
                else:
                    t = t.nxt

            result = func(*args, **kwargs)
            newNode = Node(key, result, time.time(), self.head, self.head.nxt)
            self.head.nxt = newNode
            newNode.nxt.pre = newNode
            return result

        return wrap

@Cache()
def add(x, y):
    time.sleep(2)
    return x+y

print(add(1,2))

print(add(1,2))

print(add(1,3))

print(add(1,3))