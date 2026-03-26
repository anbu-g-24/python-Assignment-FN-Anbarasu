#Day 16 Assignment


#Implement multithreading for any real time example

import threading

balance = 10000
lock = threading.Lock()

def withdraw(name, amount):
    global balance

    lock.acquire()   # lock start

    print(name, "trying to withdraw", amount)

    if balance >= amount:
        balance -= amount
        print(name, "success")
    else:
        print(name, "failed")

    print("Balance:", balance)

    lock.release()   # lock end


t1 = threading.Thread(target=withdraw, args=("User1", 7000))
t2 = threading.Thread(target=withdraw, args=("User2", 5000))

t1.start()
t2.start()

t1.join()
t2.join()

