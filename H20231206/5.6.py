# 6.	定义一个装饰器，装饰以下的hello()函数，不改变hello()函数，装饰器装饰后，hello()函数的返回值应该形如“你好呀！XX”

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "你好呀！" + result
    return wrapper

@decorator
def hello():
    return "同学"

print(hello())
