#DAY 17 Assignment


#1.Function with para ,  with return

def Login(username, password):
    if(username =="Anbu", password=="pass@123"):
        return("Valid user")
    else:
        return("Invalid user")

username = input("Enter your name :")
password = input("Enter your password :")
result = Login(username , password)
print("Login ",result)


#2.while

i=1

while i<=10:
    print(i)

    i+=1


#3.For

for i in range(1,11):
    print(i)


#4.List , set , tuple

#List

numbers =[10,20,30,40,50,10]

print(numbers)
print(numbers[1])


#Tuple

num =(10,20,30,40,50)

print(num)
print(num[3])

#Set

set ={10,20,30,40,50,20,10}

print(set)


#Dictionary


student = {
    "name": "Anbu",
    "roll": 101,
    "mark": 85
}

print(student)
print(student["name"])



#5.lambda Function

add = lambda a, b: a + b

print(add(10, 20))


