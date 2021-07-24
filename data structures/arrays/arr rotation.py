'''for _ in range(int(input())):
    n,d=map(int,input().split())
    l=input().split()
    l=(l[d:len(l)+1])+l[0:d]
    l=' '.join(i for i in l)
    print(l)'''

def arrrota(arr):
    #perform single rotation
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
    return arr

for _ in range(int(input())):
    n,d=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(d):
        arr=arrrota(arr)
    print(arr)