#Day- 13 Ass



class Employee:

    def getdata(self):
        self.name = input("Enter employee name: ")
        self.salary = int(input("Enter salary: "))

    def display(self):
        print("Name:", self.name, "Salary:", self.salary)


employees = []

for i in range(3):
    e = Employee()
    e.getdata()
    employees.append(e)

print("\nEmployee Details")

for obj in employees:
    obj.display()
