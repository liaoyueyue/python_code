# 1.	定义一个迭代器，实现指定最大值后，输出从1到该最大值的序列。

class MaxValueIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current_value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value > self.max_value:
            raise StopIteration
        else:
            result = self.current_value
            self.current_value += 1
            return result

# 使用示例
iterator = MaxValueIterator(10)
for value in iterator:
    print(value)
