"""
intern N - 1 to N 
50 days - 0 to 49 


1st day -- pass is (5000*k)  k--> kth intern

from 2nd day- day(i)=day(i-1)+5000+i

find the intern with password

[intern 1 [5000,5001,5002...],
intern 2  [] ]
"""
class intern():
    def __init__(self,days,passw) -> None:
        self.days=days
        self.passw=passw
    
def days(i,k): #i refers intern k is his day
    if i==0:
        days[i]=5000*k
    else:
        days[i]=days[i-1]+5000+i
    return days

to_interns= 2#int(input())
pass_used= 5000 #int(input())
for i in range(1,to_interns+1):
    for j in range(4):
        p=days(i,j)
    print("intern %d days %d password %d" %(i,j,p))


'''pass_list=[]
pass_list.append(intern(0,pass_used))



for i in range(to_interns):
    for j in range(50):
        pass_list[i][j]=pass_list[i-1]+5000+i
        
        
        
k=10
pas=5000

l=[0]
for i in range(1,50):
    l.append(l[i-1]+i)



        '''