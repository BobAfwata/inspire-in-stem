#!/usr/bin/python

########################
#      loops : for loop 
#      Name : Bob Afwata
#      Date : 23 / 5 / 2022
###########################

print("Number\tSquare")
print("===============")
for number in range(0,9):
    print(number)
    print("\t")
    print(number**2)



squares = []

for number in range(1,10):
    square = number ** 2
    squares.append(square)

print(squares)


# arithmetic progression
# a_{n}=a_{1}+(n-1)d


# Python Program to find Sum of Arithmetic Progression Series

a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

total = (n * (2 * a + (n - 1) * d)) / 2
tn = a + (n - 1) * d

print("\nThe Sum of Arithmetic Progression Series = " , total)
print("The tn Term of Arithmetic Progression Series = " , tn)