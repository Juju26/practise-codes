"""
#file prog
s=input().split()
l=" ".join(i for i in s[::-1])
f=open('abc.txt','w')
for j in l:
    f.write(j)
f.close()
try:
    p=open('abc.txt','r+')
    try:
        print(p.read())
    except FileNotFoundError:
        print("Quited")
#print("HERE")
except FileNotFoundError as e:
    print("exited")


n=5
k=0
for i in range(1,n):
    for j in range(1,(n-i)):
        print(end=" ")
    while k!=(2*i-1):
        print("*",end=" ")
        k+=1
    k=0
    print()
"""