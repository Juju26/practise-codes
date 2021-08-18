def nutoro(num):
    di= {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    } 
    s = ""
    for i in di:
        s += (num//i)*di[i]
        num %= i      
    return s

n=int(input())
s=nutoro(n)
print(s)