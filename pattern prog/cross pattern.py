'''
zoho qn ahm
P         M
 R      A
   O  R
     G
  O    R
 R       A
P          M
'''
s='cry'
n=len(s)
c=n-1
for i in range(0,n):
    for j in range(0,n):
        if j==c and i!=j:
            print(s[c],end='')
            c-=1
        elif i==j and i!=c:
            print(s[i],end='')
        elif i== c==j:
            print(s[i],end='')
            c-=1
        else:
            print(' ',end='')
    print()