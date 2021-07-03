import hashlib


# initializing string 
mystring = input("Enter your value: ")
  
# encoding user input value using encode() 
# then sending to md5() 
myhash = hashlib.md5(mystring.encode()) 

# printing the equivalent hexadecimal value. 
print("The md5 hash of your value is : ", end ="") 
print(myhash.hexdigest()) 
