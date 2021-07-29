l1= [1,2,3,4,5,3,5,6,7,4,1,5,7,3,8]   #list(map(int,input().split()))
l2= [6,1,2,5,4,8,2,1,4,4,2]  #list(map(int,input().split()))
dl=[]
if len(l1)==len(l2):
    for i in range(len(l1)):
        if l2[i]>=l1[i]:
            dl.append(0)
        else:
            dl.append(l2[i]) 
    for j in dl:
        print(j,end=' ')

elif len(l1)>len(l2):
    di=len(l1)-len(l2)
    for i in range(len(l2)):
        if l2[i]>=l1[i]:
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
        if l2[i]>=l1[i]:
            dl.append(0)
        else:
            dl.append(l2[i])
    s=l2[-(di)::]
    for i in s:
        dl.append(i) 
    for j in dl:
        print(j,end=' ')