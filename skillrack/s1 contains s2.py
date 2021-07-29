ts='germanactor'      #'superkoolfillerandcopperkit' #input().strip()
s='men' #input().strip()
c=0
l=[]
for i in range(len(ts)):
    try:
        if ts[i]==s[c]:
            c+=1
            l.append(ts[i])
            
    except IndexError as e:
        break 
l=''.join(i for i in l)
if l==s:
    print('yes')
else:
    print('no')