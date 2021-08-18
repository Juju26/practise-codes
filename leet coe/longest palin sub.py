class Solution:
    def longestPalindrome(self, s: str) -> str:
        st=""
        mal=0
        for i in range(len(s)):      
            if mal > 0 and (len(s)-i-1<mal//2):
                break
            l,r=i,i             #for odd len str bab
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>mal:
                    st=s[l:r+1]
                    mal=r-l+1
                l-=1
                r+=1
            
            l,r=i,i+1           #for odd len str bb
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1)>mal:
                    st=s[l:r+1]
                    mal=r-l+1
                l-=1
                r+=1
        return st