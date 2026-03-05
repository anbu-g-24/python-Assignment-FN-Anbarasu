#Day 9-10 Ass


#1.No parameters, No return type

def total_price():
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))
    total = price * quantity
    print("Total Price =", total)

total_price()

#2.with para, no return type

def total_price(price, quantity):
    total=price*quantity
    print("Total price =", total)

price=float(input("Enter product price :"))
quantity = int(input("Enter quantity :"))
total_price(price, quantity)


#3.no para, with return type

def total_price():
    price= float(input("Enter product price :"))
    quantity= int(input("Enter quantity :"))
    return price*quantity
result= total_price()
print("Total price =", result)
    

#4.with para, with return type
def total_price(price, quantity):
    return price* quantity

price=float(input("Enter product price :"))
quantity =int(input("Enter quantity"))
result=total_price(price, quantity)
print("Total price =",result)
