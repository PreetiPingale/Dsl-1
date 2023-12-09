#Bank
bal=0
c=1
def deposit():
    global bal
    am=int(input ("Enter amount to deposit "))
    bal=bal+am
    print ("Your balance is",bal)
def withdraw():
    global bal
    am=int(input("Enter amount to withdraw "))
    if bal<=0:
        print ("Withdraw not possible ")
    else:
        if bal<am:
            print ("Insufficient balance ")
        else:
            bal=bal-am
            print ("Withdraw successful ")
            print ("Your current balance is",bal)
def display ():
    print ("Your Balance is ",bal)

while c==1:
    print ("1. Deposit ")
    print ("2. Withdraw ")
    print ("3. Display ")
    print ("-----------")
    ch=int(input ("Enter choice "))
    if ch==1:
        deposit()
    elif ch==2:
        withdraw()
    elif ch==3:
        display()
    else:
        print ("Invalid Input ")
    c=int(input ("Do you want to continue yes=1 no=0"))
