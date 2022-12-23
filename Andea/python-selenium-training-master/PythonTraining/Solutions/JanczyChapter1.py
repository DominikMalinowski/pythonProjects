
# Check if input number is multiple of 4, even number, or odd number
print("Enter a number: ")

entered_number = int(input())

if entered_number % 4 == 0:
    print("You have entered multiple of 4!")
elif entered_number % 2 == 0:
    print("You have entered even number!")
else:
    print("You have entered odd number!")


# Extra part
print("Enter number to divide by: ")
check = int(input())

print("Enter number to check: ")
num = int(input())

if check % num == 0:
    print("Number divides evenly by the check number!")
else:
    print("Number doesn't divide evenly by the check number!")

