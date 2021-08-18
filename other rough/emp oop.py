from abc import ABC,abstractclassmethod

class Employee(ABC):        
    @abstractclassmethod
    def empdetails(self,id,name,age):
        pass
    def emp_type(self,age):
        if age>=20 and age<=24:
            print("Sw")
        else:
            print("MAna")

class Department(ABC):
    @abstractclassmethod
    def dept(self,dname,did):
        pass

class Softwareengineer(Employee):
    def empdetails(self,id,name,age):
        self.id=id
        self.name=name 
        self.age=age 
        print("Software Engineer")

class Manager(Employee):
    def empdetails(self, id, name, age):
        self.id=id
        self.name=name 
        self.age=age
        print("Manager")

class FinanceDept(Department):
    def dept(self, dname, did):
        return super().dept(dname, did)
class EngineeringDept(Department):
    def dept(self, dname, did):
        return super().dept(dname, did)

id=101#int(input("Enter id :"))
name= "Arun" #input("Enter name :")
age=int(input("Enter age :"))
d_name="CSE" #input("Enter dept name :")
did=12#int(input("Enter dept id :"))
emp1=Employee
emp1.empdetails(id,name,age)
dep1=Department
dep1.dept(d_name,did)
