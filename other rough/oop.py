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
    pass 

class EngineeringDepartment(Department):
    pass

age=int(input('Enter the age: '))

if age>=20 and age<=24:
    Engineer=SoftwareEngineer()
    Engineer.abstract('1','hari',age)
elif age<=30 and age>=25:
    Manager1=Manager()
    Manager1.abstract('2','hari',age)