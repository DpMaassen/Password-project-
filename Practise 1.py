# While loop integers
X = 1
while X < 5:
    X = X + 1
    print(X)
else:
    print("finished")

# while loop for a string, using password example
password = ""
number_guess = 5

while password != "safe" and number_guess > 0:
    print("enter password")
    print("you have", number_guess, "tries left")
    password = input()
    if password == "safe":
        print("password correct!")
    else:
        print("false")
        number_guess = number_guess - 1
if number_guess > 0:
    print("welcome")
else:
    print("too many wrong inserts, blocked")

# For Loop, in range(5) prints 0 to 4. Hence, the +1 in print

for Y in range(5):
    print(Y+1)
else:
    print("done")

# if loop
A = 2

if A < 3:
    print("small")
elif A == 3:
    print("same")
else:
    print("big")