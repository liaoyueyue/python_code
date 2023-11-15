# 6.	某家电卖场需要对本月部分商品销售情况进行统计,求出本月销售量最高和最低商品,以便调整销售策略,同时根据本月销售量对下月销售进行预估,判断是否要补充商品库存。请帮助卖场统计商品销售的情况，以电视机","洗衣机","冰箱","空调","热水器"为例，自拟测试数据。

# 假设的本月商品销售数据
sales_data = {
    "电视机": 120,
    "洗衣机": 90,
    "冰箱": 150,
    "空调": 80,
    "热水器": 100
}

# 求出本月销售量最高和最低的商品
max_sale_product = max(sales_data, key=sales_data.get)
min_sale_product = min(sales_data, key=sales_data.get)

print(f"本月销售量最高的商品是：{max_sale_product}，销售量为：{sales_data[max_sale_product]}")
print(f"本月销售量最低的商品是：{min_sale_product}，销售量为：{sales_data[min_sale_product]}")

# 下月销售预估
average_sales = sum(sales_data.values()) / len(sales_data)
for product, sales in sales_data.items():
    if sales > average_sales:
        print(f"商品 {product} 的销售量高于平均水平，建议补充库存。")
    else:
        print(f"商品 {product} 的销售量正常。")
