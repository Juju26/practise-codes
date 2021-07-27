def timeConversion(s):
    # Write your code here
    hr,mi,se=s.split(':')
    hr=str(hr)
    mi=str(mi)
    pf=se[-2::]  #pf= am/pm
    sec=str(se[0:2])
    if pf=='PM' and hr!='12':
        hr=str(12+int(hr))
    elif pf=='AM':
        if hr=='12':
            hr='00'
    #ti=str(hr)+':'+str(mi)+':'+str(sec)        
    ti=hr+':'+mi+':'+sec
    return ti

s = '12:05:45AM'
result = timeConversion(s)
print(result)