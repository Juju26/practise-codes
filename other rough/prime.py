'''start=-97
end=47
s=0
l=[]
for num in range (start,end):
    if num>1:
        count = 0
        for i in range(2, (num//2 + 1)):
            if(num % i == 0):
                count = count + 1
                break

        if (count == 0 and num != 1):
            l.append(num)
    elif num==0:
        pass
    elif num<1:
        num=num*-1
        count = 0
        for i in range(2, (num//2 + 1)):
            if(num % i == 0):
                count = count + 1
                break

        if (count == 0 and num != 1):
            l.append(num*-1)
            
o=l[0]+l[-1]
print(o)

n= 3 #int(input())
l=[]
k=list(map(int,input().split()))
for i in k:
    if int(i)%2==0: print(i,end=' ')
    else: l.append(i)
print(' '.join(str(j) for j in l),end='')'''

i,temp=0,0
#n = int(input("please give a number : "))
n=20
for j in range(2,20):   
    for i in range(2,j):
        if j%i == 0:
            break
    else:
        print(j,end=' ')
    