import time

print("please insert your card")

time.sleep(5)

password=1234

pin=int(input("enter your atm pin"))

balance =5000

if pin==password:
    while True:

     print("1==balance")
     print("2==withdraw balance")
     print("3==deposite balance")
     print("4==exit")
     try:
         option=int(input("please enter your choice"))
     except:
         print("please enter valid option")
     if option ==1:
         print(f"your current balance id{balance}")
         print("--------------------------------")
     if option==2:
        withdraw_amount=int(input("pease enter withdraw_amount"))
        balance=balance-withdraw_amount
        print(f"your current balance is{balance}")
        print("--------------------------------")
     if option==3:
        deposite_amount=int(input("please enter deposite_amount"))
        balance=balance+deposite_amount
        
        
        print(f"{deposite_amount} is credited to your account")
        print(f"your current balance is {balance}")
        print("--------------------------------")
     if option==4:
          break








else:
    print("wrong pin please try agin")