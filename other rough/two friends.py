"""
find days two friends could meet each other given their schedules
"""
from datetime import datetime
from collections import namedtuple

def month_nametonum(st):
    do=datetime.strptime(st,"%b")
    nu=do.month
    return nu

r=namedtuple('r',['s','e'])
"""
12Jan2019
18Jan2019
16Jan2019
18Jan2019
1 -> ip (12Jan2011)
     getting year -> 2011
     getting month -> Jan
     converting-month  
      in numbers       -> 1 (Jan)
     getting day ->  12 

doing this for friend 1 arraival , depature &
               friend 2 arraival , depature

"""
#person 1 arraival
fr1_arr=input()
fr1_a_ye=int(fr1_arr[-4:])
fr1_a_mon=fr1_arr[-7:-4]
fr1_a_monu=int(month_nametonum(fr1_a_mon))
fr1_a_day=int(fr1_arr[-9:-7])

#person 1 depature
fr1_dep=input()
fr1_d_ye=int(fr1_dep[-4:])
fr1_d_mon=fr1_dep[-7:-4]
fr1_d_monu=int(month_nametonum(fr1_d_mon))
fr1_d_day=int(fr1_dep[-9:-7])

#person 2 arraival
fr2_arr=input()
fr2_a_ye=int(fr2_arr[-4:])
fr2_a_mon=fr2_arr[-7:-4]
fr2_a_monu=int(month_nametonum(fr2_a_mon))
fr2_a_day=int(fr2_arr[-9:-7])

#person 2 depature
fr2_dep=input() 
fr2_d_ye=int(fr2_dep[-4:])
fr2_d_mon=fr2_dep[-7:-4]
fr2_d_monu=int(month_nametonum(fr2_d_mon))
fr2_d_day=int(fr2_dep[-9:-7])


r1=r(s=datetime(fr1_a_ye,fr1_a_monu,fr1_a_day),e=datetime(fr1_d_ye,fr1_d_monu,fr1_d_day))
r2=r(s=datetime(fr2_a_ye,fr2_a_monu,fr2_a_day),e=datetime(fr2_d_ye,fr2_d_monu,fr2_d_day))
fs=max(r1.s,r2.s)
le=min(r1.e,r2.e)
d=(le-fs).days+1
ov=max(0,d)
print(ov)