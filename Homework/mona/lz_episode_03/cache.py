import time
import pickle # ���������л�
import hashlib # �õ����л����ݺ���ַ���
import functools # ����ԭ����������

d_cache = {}  

def judge_time(entry, expire_date):
    d = time.time() - entry['time']
    return d > expire_date

def hash_key(funcName, args, kwargs):
    key = pickle.dumps((funcName, args, kwargs))
    return hashlib.md5(key).hexdigest()

def cache(expire_date = 3):
    def _cache(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            key = hash_key(func.__name__, args, kwargs) # �õ���״̬��hashֵ���ж��Ƿ�����
            
            # �жϲ����
            if key in d_cache and not judge_time(d_cache[key], expire_date):
                print('Hey! You have just calculated it!')
                return d_cache[key]['value']
            
            result = func(*args, **kwargs)
            d_cache[key] = {'value':result, 'time':time.time()}
            return result
        return wrap
    return _cache

@cache()
def add(x, y):
    time.sleep(2)
    return x+y

print(add(1,2))

print(add(1,2))

print(add(1,3))

print(add(1,3))