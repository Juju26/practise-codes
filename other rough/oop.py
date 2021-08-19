from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def abstract(self,id,name,age):
        pass

class Department(ABC):
    @abstractmethod
    def abstr(self,id,deptName):
        pass

class SoftwareEngineer(Employee):    
    def abstract(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
        print('SoftwareEngineer')
    
class Manager(Employee):
    def abstract(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
        print('Manager')

class FinanceDepartment(Department):
    def abstr(self, id):
        self.id=id
        self.deptName="CSE"

class EngineeringDepartment(Department):
    def abstr(self, id):
        self.id=id
        self.deptName="ECE"

age=int(input('Enter the age: '))
id=int(input("Enter id: "))
name=input("Enter name :")
depid=102
if age>=20 and age<=24:
    Engineer=SoftwareEngineer()
    Engineer.abstract(id,name,age)
    print(Engineer.__dict__)
    if depid==101:
        dep=FinanceDepartment()
        dep.abstr(depid)
        print(dep.__dict__)
    elif depid==102:
        dep1=EngineeringDepartment()
        dep1.abstr(depid)
        print(dep1.__dict__)
elif age<=30 and age>=25:
    Manager1=Manager()
    Manager1.abstract(id,name,age)
    if depid==101:
        dep=FinanceDepartment()
        dep.abstr(depid)
        print(dep.__dict__)
    elif depid==102:
        dep1=EngineeringDepartment()
        dep1.abstr(depid)
        print(dep1.__dict__)