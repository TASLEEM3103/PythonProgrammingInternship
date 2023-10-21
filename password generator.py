# Create a random password generator!

# import random library for generating random characters
import random

# import string library
import string

#gather our characters
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    # set password length
    plen = int(input("Enter password length :\n"))
    # number of passwords to generate
    no_of_pw = int(input("Enter number of passwords to generate :\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    for i in range(no_of_pw):
        #shuffling characters 
        random.shuffle(s)
        #using str.join() to concatenate any number of strings
        print(f"Your secure password {i+1} is :", "".join(s[0:plen]))    
