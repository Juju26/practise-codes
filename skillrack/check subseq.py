s= input() #"management"
ks= input() #"amet"
c=0
il=[0]
iw=[]
for i in range(len(s)):
    if s[i]==ks[c] and i>=max(il):
        c+=1
        il.append(i)
        iw.append(s[i])
if ''.join(i for i in iw)==ks: print("Found")
else: print("NotFound")