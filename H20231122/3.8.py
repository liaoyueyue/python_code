# 8.	编写函数，传入自己喜欢的景点，景点所在的省份以及省份的简称，函数用于对这些信息进行打印。
def print_favorite_spot_info(spot, province, province_abbreviation):
    print(f"我喜欢的景点是：{spot}")
    print(f"这个景点位于省份：{province}")
    print(f"省份的简称是：{province_abbreviation}")

# 调用函数并传入喜欢的景点、省份和省份简称
print_favorite_spot_info("三峡大坝", "湖北", "鄂")
