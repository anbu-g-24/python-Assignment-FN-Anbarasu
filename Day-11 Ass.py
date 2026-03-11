
#Day-11 Assignment



#1.ATM Withdrawal System

balance=0
while True:
    
    print("1.Withdrawal amount")
    print("2.Check Balance")
    print("3.Deposite")
    print("4.Exit")


    choice=int(input("Enter your choice :"))

    if choice ==1:
        amount=int(input("Enter withdraw amount :"))

        if amount<=balance:
            balance=balance-amount
            print("amount withdrawal successfuly")

        else:
            print("Insufficient balance!")
    elif choice==2:
        print("your balance is :", balance)

    elif choice==3:
        amount = int(input("Enter your deposite amount"))
        balance = balance+amount
        print("Amount deposite successfully")
    elif choice==4:
        print("Thank you!")
        break;
    else:
        print("Invalid")
 
   

#2.Number Guessing Game

import random

number= random.randint(1,10)

while True:
    guess = int(input("Guess the number(1-10) :"))

    if guess== number:
        print("you Won!")
        break;
    else:
        print("Try again")

#3.Multiplication Table Generator

num = int(input("Enter a number :"))

for i in range(1,11):
    print(i,"x",num,"=",num*i)


#4.Password Login System

correct_password ="anbu1234"

for i in range(3):
    password=input("Enter your password :")

    if password==correct_password:
        print("Login Successfully")
        break;
    else:
        print("Wrong password")
else:
    print("Account Locked")

    
username= input("Enter your username ")
password= input("Enter your password")
if (username=="Anbu" ,password=="pass@123"):
    print("Login successful")
else:
    print("Try Again")


#5.Even and Odd Counter




even = 0
odd = 0

for i in range(2):
    num = int(input("Enter number: "))

    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even count =", even)
print("Odd count =", odd)


#even or odd number


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
