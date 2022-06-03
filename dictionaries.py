#!/usr/bin/python

# Is a collection of key value pairs 

#A key-value pair is a set of values associated with each other

student = {'Name': 'Bob Afwata', 'age' : 23}

book = {'Color ': 'Green','Publisher ':'Oxford Press'}


#simplest dictionary has one key value pair 

alien_o = {'color':'green'}

# Accessing values in adictionary 

print(alien_o['color'])
print(student['Name'])
print(student['age'])


#Adding key value pairs to dict

alien_1 = {'color': 'blue','points':5 }
print(alien_1)

#add position cordinates 
alien_1['x_position'] = 45
alien_1['y_position'] = 4

print(alien_1)



#staring with empty dictionary 

student = {}
#Add pairs

student['Name'] = 'Martha Wayne'
student['Age'] = 24
print(student)


#Modifying values in a dictionary
student = {'Name': 'June'}
print("The first student  is " + student['Name'] + ".")
student['Name'] = 'John'
print("The first student  is now " + student['Name'] + ".")



#Removing key value pairs 

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)



#Dictionaries of similar data types 
favorite_languages = {'Jane':'javascript','Martha':'python','Jim':'C#','Julie':'Ruby'}
print("Jim's favorite language is " +
favorite_languages['Jim'].title() +
".")


#Loops : Using loops through dictionaries

#For loop
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

