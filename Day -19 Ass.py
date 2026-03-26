#Day 19 Assignment

#create aclass and object
#-------------------------------

class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

    def display(self):
        print("Name :", self.name)
        print("Mark :", self.mark)

    def result(self):
        if self.mark >=50:
            print(self.name,"Pass")
        else:
            print(self.name,"Fail")


s1 = Student("Anbu",95)
s2 = Student("santhosh",90)

s1.display()
s1.result()

print("---------------")


s2.display()
s2.result()
