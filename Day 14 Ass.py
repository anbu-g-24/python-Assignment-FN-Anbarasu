#1.if else

num = int(input("Enter the number :"))

if num>=1:
    print("Passitive number ")
else:
    print("negative number ")


#2.while

i=1
while i<=10:
    print(i)
    i=i+1

#3.For loop

for i in range(1,11):
    print(i)

#4.class and object


class shapes:

    def triangle(self):
        print("triangle is a 15 cm")

a = shapes()
a.triangle()

#5.inheritance


class A:
    def show(self):
        print("This is class A")

class B(A):
    def display(self):
        print("This is class B")

obj = B()

obj.show()
obj.display()


#6.List

names = ["Dinesh","Santhosh","Anbu","Jeeva","Jawahar"]

for n in names:
    print(n)

#7.Tuple

colors = ("red", "green", "blue")

for c in colors:
    print(c)
