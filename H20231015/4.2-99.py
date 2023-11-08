for i in range(1, 10):
    for j in range(1, i+1):
        result = i * j
        print(f"{i} x {j} = {result}", end="\t")
    print()

print("--------------------------------------------------------------------------------------")
for i in range(1, 10):
    for s in range(1,i):
        print(end=" "*12)
    for j in range(i,10):
        result = i * j
        print(f"{i} x {j} = {result}", end="\t")
    print()