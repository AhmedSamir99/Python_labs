import mysql.connector
from getpass import getpass

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database='python'
)

class Employee:
    # Static list contains all employee
    all_employees = [] 

    def __init__(self, First_name, Last_name, Age, Department, Salary):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Age = Age
        self.Department = Department
        self.Salary = Salary
        self.id=None
        Employee.all_employees.append(self)
        self.add_employee_to_database()

    def add_employee_to_database(self):
        with mydb.cursor() as cur:
            sql = "INSERT INTO employees (First_name, Last_name, Age, Department, Salary) VALUES (%s, %s, %s, %s, %s)"
            values = (self.First_name, self.Last_name, self.Age, self.Department, self.Salary)
            cur.execute(sql, values)
            mydb.commit()
            self.id=cur.lastrowid

    # @staticmethod
    def transfer(self,emp_id, department):
        with mydb.cursor() as cur:
            sql = "UPDATE employees SET Department=%s WHERE id=%s"
            values = (department, emp_id)
            cur.execute(sql, values)
            mydb.commit()

    
    def fire(self):
        Employee.all_employees.remove(self)
        with mydb.cursor() as cur:
            sql = "DELETE FROM employees WHERE id=%s"
            values = (self.id,)
            cur.execute(sql, values)
            mydb.commit()
            # cur.execute("DELETE FROM employee WHERE id = %s", (self._id,))
            Employee.employee_list.remove(self)
        
    def showEmployeeData(self):
        with mydb.cursor() as cur:
            sql = "SELECT * FROM employees WHERE id=%s"
            values = (self.id,)
            cur.execute(sql,values)
            # mydb.commit()
            data = cur.fetchall()
            for row in data:
                print(row)
    # static 
    @staticmethod
    def show_all_employees():
        with mydb.cursor() as cur:
            sql = "SELECT * FROM employees"
            cur.execute(sql)
            data = cur.fetchall()
            for row in data:
                print(row)
    

class Manager(Employee):
    def __init__(self, First_name, Last_name, Age, Department, Salary,Managed_department):
        super().__init__(First_name, Last_name, Age, Department, Salary)
        self.Managed_department = Managed_department

    def showEmployeeData(self):
        with mydb.cursor() as cur:
            sql = "SELECT First_name, Last_name, Age, Department  FROM employees WHERE Department=%s"
            values = (self.Managed_department,)
            cur.execute(sql,values)
            data = cur.fetchall()
            
            for row in data:
                print(row)
    
    # def show(self):
    #     print(f"First Name: {self.First_name}")
    #     print(f"Last Name: {self.Last_name}")
    #     print(f"Age: {self.Age}")
    #     print(f"Department: {self.Department}")
    #     print("Salary: confidential")


# Ahmed = Employee("Ahmed", "Ali", 22, "IT", 50000)
# Ali = Employee("Ali", "Ahmed", 22, "IT", 50000)
# Samar = Employee("Samar", "Ahmed", 22, "IT", 50000)
# Alia= Employee("Alia", "Ahmed", 22, "IT", 50000)


# Mona = Manager("Mona", "Ahmed", 22, "IT", 50000, "IT_office")

# Mona.showEmployeeData()

# Ahmed.showEmployeeData()
# Employee.show_all_employees()

# # Shar7 elbashmohandes
# class Organization:
#     IT= 'ITI'
#     HR= 'HR'
#     Finance= 'Finance'
#     Marketing= 'Marketing'

#     @classmethod
#     def set_salary(cls, name_of_dept):
#         if cls.IT == name_of_dept:
#             pass
#         elif cls.HR == name_of_dept:
#             pass
#         elif cls.Finance == name_of_dept:
#             pass
#         else:
#             pass

# class Company(Organization):
#     pass        


def main():
    while True: #make the code run except the user wants to exit 
        print("Select an operation:")
        print(" Enter (e) to Add new employee")
        print(" Enter (m) to Add new manager")
        print(" Enter (t) to Transfer employee")
        print(" Enter (s) to Show employee/manager")
        print(" Enter (l) to List all employees/managers")
        print(" Enter (f) to Fire employee/manager")
        print(" Enter (q) to Quit")
        
        operation = input("Enter the operation you want: ")
        
        if operation == 'e':
            addEmployee()
        elif operation == 'm':
            addManager()
        elif operation == 't':
            transferEmployee()
        elif operation == 's':
            showEmployee()
        elif operation == 'l':
            listEmployees()
        elif operation == 'f':
            fireEmployee()
        elif operation == 'q':
            break
        else:
            print("Invalid operation")


#make an instance of employee class    
def addEmployee():
    print("Adding new employee:")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    dept = input("Department: ")
    salary = int(input("Salary: "))
    Employee(first_name, last_name, age, dept, salary)
    print("Employee added successfully")

#make an instance of manager class  
def addManager():
    print("Adding new manager:")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = int(input("Age: "))
    dept = input("Department: ")
    salary = float(input("Salary: "))
    managed_department = input("Managed department: ")
    Manager(first_name, last_name, age, dept, salary, managed_department)
    print("Manager added successfully")


def transferEmployee():
    id = int(input("Enter employee/manager ID: "))
    dept = input("Enter new department: ")
    emp = findEmployee(id)
    if emp:
        emp.transfer(dept)
        print("Employee/manager transferred successfully")
    else:
        print("Employee/manager not found")

def showEmployee():
    id = int(input("Enter employee/manager ID: "))
    emp = findEmployee(id)
    if emp:
        emp.show()
    else:
        print("Employee/manager not found")

def listEmployees():
    print("All employees/managers:")
    Employee.show_all_employees()

def fireEmployee():
    id = int(input("Enter employee/manager ID: "))
    emp = findEmployee(id)
    if emp:
        emp.fire()
        print("Employee/manager fired successfully")
    else:
        print("Employee/manager not found")

#find the employee/manager in the list 
def findEmployee(id):
    for emp in Employee.all_employees:
        if emp._id == id:
            return emp
    return None

if __name__ == '__main__':
    main()