# to print
# 1 2 3 4
# 2 3 4
# 3 4
# 4

a=0
for i in range(4):

    for j in range(4-i):
        a+=1
        print(a,end="")
    a=i
    a+=1
    print()