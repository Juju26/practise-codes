s='cypatlyrmenomesloanueeleuap'
#madeinindiaz
n=9
"""
m i d 
a n i
d i a
e n z
"""
l=[]
c=0
for i in range(0,len(s),n):
    p=s[i:i+n]
    if c%2!=0:
        l.append(p[::-1])
    else:
        l.append(p)
    c+=1
o=''
print(l)
for i in range(n):
    for j in range(len(l)):
        o+=l[j][i]
print(o)