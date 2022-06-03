
acc_bal = input("Enter your acc balance :")

if(int(acc_bal) > 100000  and int(acc_bal) < 200000):
    acc_bal = acc_bal - 25000
    print(" We have deducted ksh 25000")
else if (int(acc_bal) > 500000  and int(acc_bal) < 1000000):
    acc_bal = acc_bal - (0.3*acc_bal)
    print("We have deducted 30 percent   from your account ")
else if int(acc_bal) > 1000000:
        acc_bal = acc_bal - 15000
        print("We have dedected ksh 15000 from your acc")

