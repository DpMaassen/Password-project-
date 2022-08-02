#while loop for a string, using password example.

# initializing variables 
password = ""
number_guess = 5

# Running the password loop.

while password != "safe" and number_guess > 0:
    print("enter password")
    print("you have", number_guess, "tries left")
    password = input()
    if password == "safe":
        print("password correct!")
    else:
        print("false")
        number_guess = number_guess - 1
        
# while out of the loop check if password input was correct (within) 5 tries.        
if number_guess > 0:
    print("welcome")
else:
    print("too many wrong inserts, blocked")
