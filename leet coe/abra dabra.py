mal=0
st=""
def longestPalindrome(s) -> str:
    
    def whi(l,r):
        global st
        global mal
        while l>=0 and r<len(s) and s[l]==s[r]:
            if(r-l+1)>mal:
                st=s[l:r+1]
                mal=r-l+1
            l-=1
            r+=1
        return st

    for i in range(len(s)):      
        if mal > 0 and (len(s)-i-1<mal//2):
            break
        l,r=i,i             #for odd len str bab
        r1=whi(l,r)
    
    
    for i in range(len(s)):      
        if mal > 0 and (len(s)-i-1<mal//2):
            break
        l,r=i,i+1             #for odd len str bab
        r2=whi(l,r)
    return max(r1,r2)

ip="abb"
print(longestPalindrome(ip))