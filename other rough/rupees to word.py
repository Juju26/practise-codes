def eval1(x):
    #print(x)
    ones={"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":""}
    tens={"2":"twenty","3":"thirty","4":"fourty","5":"fifty","6":"sixty","7":"seventy","8":"eighty","9":"ninety","0":""}
    elvs = {"1":"eleven","2":"twelve","3":"thirteen","4":"fourteen","5":"fifteen","6":"sixteen","7":"seventeen","8":"eighteen","9":"nineteen","0":"ten"}
    if len(x)==1:
        return ones[x[-1]]
    elif len(x)==2 and x[-2]=="1":
        return elvs[x[-1]]
    elif len(x)==2:
        return tens[x[-2:-1]]+" "+ones[x[-1]]
    elif len(x)>2:
        k=""
        if x[-2]!="0" or x[-1]!="0":
            k= ones[x[-3]]
            if x[-3]!="0":
                k = k +" hundred and "
            #k = k + "and"
            if x[-2]=="1":
                k = k + elvs[x[-1]]
            else:
                k = k + tens[x[-2:-1]]+" "+ones[x[-1]]
            return k
        else:
            if x[-3]!="0":
                return ones[x[-3]]+" hundred"
            else:
                return ""


n=input("Enter amount : ")
if not n.isnumeric():
    print ("not a number")
    
    
print(n)
n=str(int(n))
if(len(n)<=3):
    #print(1)
    print(eval1(n[0-len(n):]))
    
elif(len(n)<=5):
    #print(2)
    print(eval1(n[0-len(n):-3]),end='')
    if int(n[0-len(n):-3])!=0:
        print(" thousand",end='')
    print(eval1(n[-3:]))
        
elif(len(n)<=7):
    #print(3)
    print(eval1(n[0-len(n):-5]),end='')
    if int(n[0-len(n):-5])!=0:
        print(" lakh ",end='')
    print(eval1(n[-5:-3]),end='')
    if int(n[-5:-3])!=0:
        print(" thousand ",end='')
    print(eval1(n[-3:]))
    
elif(len(n)<=9):
    #print(4)
    print(eval1(n[0-len(n):-7]),end='')
    if int(n[0-len(n):-7])!=0:
        print(" crore ",end='')
    print(eval1(n[-7:-5]),end='')
    if int(n[-7:-5])!=0:
        print(" lakh ",end='')
    print(eval1(n[-5:-3]),end='')
    if int(n[-5:-3])!=0:
        print(" thousand ",end='')
    print(eval1(n[-3:]))

else:
    print("too big number😅")