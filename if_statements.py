cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())



age = 24 

if age != 16:
     print("Hello you are not 20 daaah")


# Checking MUltiple conditions 

# using and 

gender = 'male'
age  = 12 

if (gender == 'male') and (age < 10):
    print("You are the right candidate")
else:
    print("Sorry next time")



#checking for users in a list 

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")


# if 
age = 19 

if age >= 18:
    print("You are old enough to vote ")



#if else 
if age >= 18:
    print("You are old enough to vote ")
else:
    print("You are too young to vote ")

    