s= "management"
ks="ampt"
c=0
fl=0
il=[0]
iw=""
for i in range(len(s)):
    if s[i]==ks[c] and i>=max(il):
        c+=1
        il.append(i)
        iw+=s[i]
        if iw==ks:
            fl=1
            print("Found")
            break
if fl==0:
    print("Not found")