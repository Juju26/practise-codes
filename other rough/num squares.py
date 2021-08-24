n=144  #int(input())
su_l=[]
su=[]
su_l.append(n)
def sf(n):
    s=0
    while n>0:
        re=n%10
        s+=re**2
        n=n//10
    if s not in su_l:
        su_l.append(s)
    return s

for i in su_l:
    p=sf(int(i))
    if p in su:
        print("breaked %d" %(p))
        break
    else:
        su.append(p)
print(su_l)