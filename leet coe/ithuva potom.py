def expa(s,l,h)->str:
    le=len(s)
    while l>=0 and h<le and s[l]==s[h]:
        l-=1
        h+=1
    return s[l+1:h] 

def fin(st):
    max_s=""
    max_le=0
    for i in range(len(st)):  #n
        
        cur_str=expa(st,i,i)
        print("str 1 : ",cur_str)
        cur_le=len(cur_str) 
        if cur_le>max_le:
            max_s=cur_str
            max_le=cur_le
        cur_str1=expa(st,i,i+1)
        print("Str 2: ",cur_str1)
        cur_le1=len(cur_str1)  
        if cur_le1>max_le:
            max_s=cur_str1
            max_le=cur_le1
        print("MAx string : ",max_s)
    return max_s

s="abdbc"
print(fin(s))