class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, age):
        result = [emp for emp in self.employees if emp.age == age]
        return result

    def search_by_name(self, name):
        result = [emp for emp in self.employees if emp.name == name]
        return result

    def search_by_salary(self, operator, value):
        if operator == ">":
            result = [emp for emp in self.employees if emp.salary > value]
        elif operator == "<":
            result = [emp for emp in self.employees if emp.salary < value]
        elif operator == ">=":
            result = [emp for emp in self.employees if emp.salary >= value]
        elif operator == "<=":
            result = [emp for emp in self.employees if emp.salary <= value]
        else:
            result = []
        return result

def main():
    emp_table = EmployeeTable()

    emp1 = Employee("161E90", "Raman", 41, 56000)
    emp2 = Employee("161F91", "Himadri", 38, 67500)
    emp3 = Employee("161F99", "Jaya", 51, 82100)
    emp4 = Employee("171E20", "Tejas", 30, 55000)
    emp5 = Employee("171G30", "Ajay", 45, 44000)

    emp_table.add_employee(emp1)
    emp_table.add_employee(emp2)
    emp_table.add_employee(emp3)
    emp_table.add_employee(emp4)
    emp_table.add_employee(emp5)

    print("Search Parameters:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        age = int(input("Enter age to search: "))
        result = emp_table.search_by_age(age)
    elif choice == 2:
        name = input("Enter name to search: ")
        result = emp_table.search_by_name(name)
    elif choice == 3:
        operator = input("Enter operator (>, <, <=, >=): ")
        value = int(input("Enter salary value: "))
        result = emp_table.search_by_salary(operator, value)
    else:
        print("Invalid choice")
        return

    if not result:
        print("No matching records found.")
    else:
        print("Matching Records:")
        for emp in result:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    main()
