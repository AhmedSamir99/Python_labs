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
    employee_list = []

    def __init__(self, First_name, Last_name, Age, Department, Salary):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Age = Age
        self.Department = Department
        self.Salary = Salary
        self.id=None
        Employee.employee_list.append(self)
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

    # @staticmethod
    def fire(self):
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
    
    @classmethod
    def show_all_employees(cls):
        with mydb.cursor() as cur:
            sql = "SELECT * FROM employees"
            cur.execute(sql)
            data = cur.fetchall()
            for row in data:
                print(row)
    



Ahmed = Employee("Ahmed", "Ali", 22, "IT", 50000)
Ali = Employee("Ali", "Ahmed", 22, "IT", 50000)
Samar = Employee("Samar", "Ahmed", 22, "IT", 50000)
Alia= Employee("Alia", "Ahmed", 22, "IT", 50000)

# Ahmed.showEmployeeData()
Employee.show_all_employees()