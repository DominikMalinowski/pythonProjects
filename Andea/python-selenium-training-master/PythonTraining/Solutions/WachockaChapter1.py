"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
to the user.
Implement also check if user put the number or string.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

userNumber = int(input("Hello! Give me any number other than 0, please"))       # default data type for input() is STRING

# check if userNumber is an integer
if not str(userNumber).isnumeric():         # isnumeric() - can only be invoked on STRINGS!
   print("What you entered is not a number.")

# checking divides
if userNumber % 4 == 0:
    print("Your number is even and divisible by four.")
elif userNumber % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

# Extra 2:
print("Give me any number again.")
num = int(input())
if num == 0:
    print("You cannot divide a zero. Try a different number.")

print("Excellent. Now give me another number to divide your previous number by.")
check = int(input())
if check == 0:
    print("You can't divide by zero! Do you want the universe to explode?")

if num % check == 0:
    print(str(num) + "divides evenly by" + str(check))
else:
    print(str(num) + "divides by" + str(check) + "with a remainder.")
