# def palin(x):
#     if x>0:
#         s=str(x)
#         rs=s[::-1]
#         if s==rs:
#             return 'true'
#         else:
#             return 'false'
#     else:
#         return 'false'     
# x=int(input())
# print(palin(x))

#one liner
#return True if str(x)==str(x)[::-1] else False  
def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])

word='malayalam'
print(ispalindrome(word))