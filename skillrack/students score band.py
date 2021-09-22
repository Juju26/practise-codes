s=int(input())
p=list(map(int,input().split()))
counts = [0 for i in range(10)]
for i in range(len(p)):
    if p[i]%10==0 and p[i]!=0:
        counts[p[i]//10 - 1] += 1
    else:
        counts[p[i]//10] += 1

for i in range(10):
    if i==0:
        print('Band '+str(i*10)+'-'+str((i+1)*10)+':',counts[i]) 
    else:
        print('Band '+str(i*10+1)+'-'+str((i+1)*10)+':',counts[i])