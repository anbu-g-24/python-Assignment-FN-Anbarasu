#Day 15 Assignment

class BalanceError(Exception):
    pass

balance=10000
withrawal =int(input("Enter withrawal amount :"))

try:

    if withrawal>balance:
        
        raise BalanceError("insufficents balance")
        

    else:
        Account_balance = balance - withrawal
        print("Withrawal Successful")

        print("Remaining Balance :",Account_balance)
        

except BalanceError as e:
    print(e)
    
finally:
    print("Thank You")
