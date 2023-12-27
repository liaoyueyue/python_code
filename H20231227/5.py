# 已知 dicta = {‘a’:1,’b’:2,’c’:3,’d’:4,’f’:’hello’}，
# dictb = {‘b’:3,’d’:5,’e’:7,’m’:9,’k’:’world’}，要求写一段代码，实现两个字典的相加，不同的key对应的值保留，相同的key对应的值相加后保留，如果是字符串就拼接，输出如上示例得到的结果。

dicta = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 'hello'}
dictb = {'b': 3, 'd': 5, 'e': 7, 'm': 9, 'k': 'world'}
result = {}
for key, value in dicta.items():
    if key in dictb:
        if isinstance(value, str) and isinstance(dictb[key], str):
            result[key] = value + dictb[key]
        else:
            result[key] = value + dictb[key]
    else:
        result[key] = value
for key, value in dictb.items():
    if key not in dicta:
        result[key] = value
print(result)
