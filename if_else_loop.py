#!/usr/bin/python

sum_nums = 0
prod_nums = 1
# sum of even numbers btn 0 and 20 
for number in range(0,20):
    if(number %2 == 0):
        sum_nums = sum_nums + number
        

print(sum_nums)
# product of odd numbers btn 0, 20

for number in range(0,6):
    if(number %2 == 1): #odd number 
        prod_nums = prod_nums * number
        
        
print(prod_nums)



num = 10 
while num < 10 :
    if(num % 2 == 0):
        print(num)
    num = num + 1