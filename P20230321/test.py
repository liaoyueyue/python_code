# python中不同层级的代码必须强制要求缩进，并且相同层级的代码要求缩进的空格数量一致


# 1.1
totalWeight = 55 + 55

print(totalWeight)

# 1.2
myWeight = 95

canRide = True

if myWeight > canRide:
    print("超过体重限制")
    canRide = False

print(f"能否乘坐: {canRide}")

# 1.3
myWeight = 70.5
yourWeight = 81.3
if myWeight < yourWeight:
    print(f"myWeight:{myWeight}\nyouWeight:{yourWeight}\nyou are heavier than me")