#! /usr/bin/python
###########################
# For loops with lists
#     Name : Bob Afwata
#     Date : 24 /5/2022
#for loops 


squares = [] # empty list

for number in range(0,10):
    square = number **2 
    squares.append(square)

print(squares)