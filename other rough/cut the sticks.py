l=[5,4,4,2,2,8]
p=l[:]
print(p)
w=[]
le=len(l)
sm=min(l)
while le>1:
    c=0
    for i in range(len(p)):
        if sm==p[i]:
            p[i]=-1
            le-=1
            
        elif p[i]!=-1:
            p[i]=p[i]-sm
    for j in p:
        if j!=-1:
            c+=1
    w.append(c)
    print(w)