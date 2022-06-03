city = "Nairobi"
print(city[:5])
print(city[2:])



f_name = "bob afwata " # small letters 
# .upper() convert to upper case
print(f_name.upper())

s_name = "KENNEDY MUOKI"
# .lower() convert to lower case 
print(s_name.lower())


#concatination -converting from one data type to another 
# int -> float   float(x)
# float -> int   int(x)
# int -> string   str(x)
number = 6
print(str(number))

x = 4 #x is an integer 
print(float(x))

y = 3.24
print(int(y))

f_name = "James"

s_name = "Corden"

full_name = f_name + s_name

print(full_name)


msg = "Hello from Bob Afwata  how are you "
print(msg.split())

print(len(msg))