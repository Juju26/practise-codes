def dayOfProgrammer(year):
    # Write your code here
    if year>1918:
        if ((year%4==0 and year%100!=0) or year%400==0):
            s='12.09.'+str(year) 
        else:
            s='13.09.'+str(year) 
    elif year<1918:
        if year%4==0:
            s='12.09.'+str(year)
        else:
            s='13.09.'+str(year) 
    elif year==1918:
            s='26.09.1918' 
        
    return s    

year =1918   #int(input().strip())
result = dayOfProgrammer(year)
print(result) 

'''
-------256th day ---------
1918  : '26.09.1918

<1918 : leap year(%4 alone) -> 12.09.year
        non leap year       -> 13.09.year

>1918 : leap year(%400 or %4 and !%100) -> 12.09.year
        non leap year                   -> 13.09.year
'''  