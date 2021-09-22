s='game will mark the first time the venue is hosting an international match since 2015'
s=list(s.split())
print(s)
nor_c,rev_c=[200],[200]
w1='the'
w2='will'
for i in range(len(s)):
    if s[i]==w1:
        c=1
        for j in range(i+1,len(s)):
            if s[j]==w2:
                nor_c.append(c)
                break
            else:c+=1 
s=s[::-1]
for i in range(len(s)):
    if s[i]==w1:
        c=1
        for j in range(i+1,len(s)):
            if s[j]==w2:
                rev_c.append(c)
                break
            else:c+=1 
print(min(min(nor_c),min(rev_c)))





'''while True:
    try:
   
        p=abs(s.index(w1)-s.index(w2))
        l.append(p)
        print('p val :',p)
        if p==1:
            print('if 1',p)
            break
        else:
            s.remove(w1)
            s.remove(w2)
    except ValueError:
        print(min(l))
        break '''