

class employee:
    salary_raise = 1.05
    def __init__(self,name,age,hr_depart,qualification,salary):
        self.name= name 
        self.age= age
        self.hr_depart= hr_depart
        self.qualification= qualification
        self.salary=salary
    
    # doesnt make the class atribute and the function name same 
    def get_name (self):
        return 'The name of the employee is ' + self.name
    def get_age(self):
        return 'The age of the employee is '+ self.age
    
    def raised_salary(self):

        self.salary = int (self.salary * employee.salary_raise)


emp_1=employee("Asim","21","compsci","masters",50000)
emp_2=employee("Ram","22","compsci","masters",40000)
print(employee.get_name(emp_1))
print( emp_1.salary)

emp_1.raised_salary()

print(emp_1.salary)
 

# print(employee.get_name(emp_1))




 

