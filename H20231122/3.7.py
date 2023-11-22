# 7.	自定义一个函数，求字典中值最大的元素。利用自定义的函数找出下面A组中身高最高的人。A= {'李明': 1.78, '王强': 1.73, '金星': 1.85, '孙国涛': 1.77}
def max_value_in_dict(dictionary):
    if not dictionary:
        return None

    max_key = max(dictionary, key=dictionary.get)
    return max_key, dictionary[max_key]

A = {'李明': 1.78, '王强': 1.73, '金星': 1.85, '孙国涛': 1.77}

# 使用自定义函数找出身高最高的人
highest_person, highest_height = max_value_in_dict(A)

print(f"身高最高的人是 {highest_person}，身高为 {highest_height} 米。")
