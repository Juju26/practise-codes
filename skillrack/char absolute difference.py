s1= 'abcdxyza' #'aaaaaaaa' #input().strip()
s2= 'bcdxmnomm' #'bbbbbbbcccccc' input().strip()
l1=list(set(s1))
l2=list(set(s2))
cc=0
uc=0
for i in range(len(l1)):
    if l1[i] in l2:
        cc+=1
    else:
        uc+=1
for j in range(len(l2)):
    if l2[j] in l1:
        cc+=1
    else:
        uc+=1
print(cc,uc)
print(abs(cc-uc))
