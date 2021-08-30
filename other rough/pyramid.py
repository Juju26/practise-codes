s=5 #int(input())
for i in range(0,s):
    for j in range(s-i):
        print(" ",end=" ")
    for j in range(1,i):
        print("*",end=" ")
    for i in range(i,0,-1):
        print("*",end=" ")
    print()
