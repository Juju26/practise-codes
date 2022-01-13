# python does'nt support method overloading 
# we can't have same method name twice in a class [note: it wont give error but implements the latest method defination]
# so to implement overloading we declare variables of type none and 
#         replace its value upon passing paramenter (line 10 : m3=none )

# also we need can check number of parameters by conditions(line no:17)


class overload:
    def __init__(self,m1,m2,m3=None) -> None:
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    
    def sum(self):
        if self.m3==None:
            return self.m1+self.m2
        else: return self.m1+self.m2+self.m3
    # def sum(self):
    #     return self.m1+self.m2

obj1=overload(100,200)
print(obj1.sum())
obj2=overload(100,400,500)
print(obj2.sum())
