'''
1
21
123
4321
12345
'''
n=int(input())
for i in range(n):
    if i%2==0:
        for j in range(i+1):
            print(j+1,end='')
    elif i%2!=0:
        for j in range(i+1,0,-1):
            print(j,end='')
    print()

'''
kums solution
n = 5
for i in range(1,n+1):  # 1 2 3... n  [rows]
    for j in range(1,i+1):  # 1 2 3.. i  [columns]
        if i%2!=0:
            print(j,end='')
        else:
            print(i-j+1,end='')
    print()'''