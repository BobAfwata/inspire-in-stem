# initializing strings

name = "Bob Afwata"

# Multiline strings 

msg = ''' QRST126XDG MPESA confirmed
        you have recieved ksh 2300 from
        James Muoki .
        18th May 2022
        Safaricom transparent for you 
        '''
print(msg)
txt = """ Holla ! I am Bob Afwata
          I come from Kiambu county, Lari sub county
          I love to read ,write and dance
        """
print(txt)


#Slice From the Start
# By leaving out the start index, the range will start at the first character:
# Get the characters from the start to position 5 (not included):



city = "Nairobi"
print(city[:5])

#Slice To the End
#By leaving out the end index, the range will go to the end:
print(city[2:])

#Negative Indexing
# negative indexes to start the slice from the end of the string:

print(city[-1]) # try - 2


#modifying strings 
#Upper case and lower case 

f_name = "bob "
s_name = "AFWATA"

print(f_name.upper())

print(s_name.lower())


#Removing white spaces

msg = " Hello, World!                          "
print(msg.strip()) # returns "Hello, World!"



#The replace() method replaces a string with another string:

name = "Brett Cooper"

print(name.replace('t','G'))

#The split() method returns a list where the text between the specified separator becomes the list items.

msg = "Hello from Bob Afwata "
print(msg.split())