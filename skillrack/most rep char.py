#s=input().split()
s='apple'
si=s[::] 
coli=[]
for i in set(si):
    coli.append(si.count(i))
mco=max(coli)
for i in si:
    if si.count(i)==mco:
        print(i,end='')