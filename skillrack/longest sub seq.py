s1="britanica"  #input()
s2="rtiac"  #input()
if len(s1)<len(s2):
    ss=s1
    bs=s2 
else:
    ss=s2
    bs=s1 
c=0
co=0
for i in range(len(ss)): 
    if ss[i] in bs[c:len(bs)+1]:
        co+=1 
        print(bs[c:len(bs)+1])
        c=i+1
print("ss",co)