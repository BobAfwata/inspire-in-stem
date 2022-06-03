age = input("What is your age ? ")


acc_bal = 0

if (int(age) > 25) and (int(age) < 30 ):
    acc_bal = acc_bal + 10000
    print("Confirmed You have recieved ksh 10000")
else:
    print("Sorry no money for you")
