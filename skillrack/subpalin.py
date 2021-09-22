s='delegate' #input()
c=0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        p=s[i:j]
        print(p)
        if p==p[::-1] and len(p)>=2:
            print("cou :",p)
            c+=1
print(c)