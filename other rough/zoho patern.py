'''
n=5
1
1 1 
2 1
1 2 1 1
1 1 1 2 2 1


count followed by number

'''
'''
n=5 
l=[2,1]
p=[]
print(l[0])
for i in range(n-1):
    for j in range(len(l)):
        if j!=len(l)-1:
            if l[j]==l[j+1]:
                p.append(l[j])
                print('p= ',p) 
            else:
                p.extend([len(p),p[0]])
                print(p)
                l=p[0::]
                p=[]'''
l=[1]
print(1)
l=[1,1]
