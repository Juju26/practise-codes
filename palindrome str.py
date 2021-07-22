def palin(x):
    if x>0:
        s=str(x)
        rs=s[::-1]
        if s==rs:
            return 'true'
        else:
            return 'false'
    else:
        return 'false'     
x=int(input())
print(palin(x))

#one liner
#return True if str(x)==str(x)[::-1] else False  
