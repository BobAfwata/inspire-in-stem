# A list is a collection of items in a particular order

# use [ ']
fruits = ['Mango', 'banana', 'lime', 'Orange']
print(fruits)

# Accessing Elements in a List use the index / position
# INdex begins with 0

print(fruits[0])

print(fruits[3].title()) # try fruits[-1] and fruits[7]
print(fruits[-1].title()) # Why ????
# print(fruits[7].title())

# Using a list element 

print("My favourite fruit is " + fruits[2].title() + ".")

# Changing, adding, and removing elements

cities = ['New York', 'London', 'Nairobi','Tokyo']
print("Original Cities -> " , cities)
cities[0] = 'Kampala'
print("Cities after change ->  ",cities)

