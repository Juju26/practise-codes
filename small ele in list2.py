l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
dl=[]
if len(l1)==len(l2):
    for i in range(len(l1)):
        if l2[i]>l1[i]:
            dl.append(0)
        else:
            dl.append(l2[i]) 
    for j in dl:
        print(j,end=' ')

elif len(l1)>len(l2):
    di=len(l1)-len(l2)
    for i in range(len(l2)):
        if l2[i]>l1[i]:
            dl.append(0)
        else:
            dl.append(l2[i]) 
    s=l1[-(di)::]
    for i in s:
        dl.append(i)
    for j in dl:
        print(j,end=' ') 

elif len(l1)<len(l2):
    di=len(l2)-len(l1)
    for i in range(len(l1)):
        if l2[i]>l1[i]:
            dl.append(0)
        else:
            dl.append(l2[i])
    s=l2[-(di)::]
    for i in s:
        dl.append(i) 
    for j in dl:
        print(j,end=' ')