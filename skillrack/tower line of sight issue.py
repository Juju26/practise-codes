s1='0 0'
s3='2 0'

s2='-2 0'
s4='-5 0'

ax,ay=map(int,s1.split())
bx,by=map(int,s2.split())
cx,cy=map(int,s3.split())
dx,dy=map(int,s4.split())
l=[]
p=[]
fl=0
mia=min(ay,cy)
maa=max(ay,cy)

if ax!=cx:
    for i in range(ax,cx+1):
        if ay!=cy:
            for j in range(mia,maa+1):
                l.append([i,j])
        else:
            l.append([i,cy])
else:
    for j in range(mia,maa+1):
        l.append([ax,j])

print(l)
mi=min(by,dy)
ma=max(by,dy)

if bx!=dx:
    for i in range(bx,dx+1):
        if by!=dy:
            
            for j in range(mi,ma+1):
                p.append([i,j])
        else:
            p.append([i,dy])
else:
    for j in range(mi,ma+1):
        p.append([bx,j])

print(p)
for i in l:
    if i in p:
        fl=1
        break
if fl==0:
    print('no')
else:
    print('yes')