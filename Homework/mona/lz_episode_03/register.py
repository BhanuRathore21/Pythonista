import functools
d_fun={}

def register(fn):
    d_fun.update({fn.__name__:fn})
    @functools.wraps(fn)
    def wrap(*args, **kwargs):
        #d_fun.update({fn.__name__:fn})
        ret = fn(*args, **kwargs)
        return ret
    return wrap

def cmd():
    end = 'exit'
    while True:
        c = input('>>����������:')
        if c==end:
            break
        if c in d_fun:
            para = input('>>���������:')
            s_para = para.split(',')
            t = []
            for x in s_para:
                t.append(int(x))
            print('>>���:',d_fun[c](*t))
        else:
            print('?û�д�������o')
@register
def add(x,y):
    return x+y
@register
def multi(x,y):
    return x*y

cmd()