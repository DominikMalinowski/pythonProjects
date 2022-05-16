"""
Create app to send money with inputs:
 - recipient's name - string without digits
 - choice of payment method - 1. account number, 2. phone number - possible to choose a number
 - account number or phone number depending on previous choice
 - title - max 50 characters - can be empty
 - currency - $, PLN, EURO - possible to choose a number
 - transfer amount - max value depending on currency choice - 1000PLN, 300 EURO, 400$
 - date of the transfer - with input format m.d.y
 - confirmation of payment - YES/NO
After confirming the transfer display the message "Money have been sent. Would you like to receive an email confirmation":
  - if Yes - Enter email, and display "Confirmation has been sent"
  - if No - finish the program
"""
# Modules import section
import pyinputplus as pyip

# Saving input to file
with open('.\money.txt', 'w') as file:

    # Recipient name input + validation
    recipient_name = pyip.inputRegex(r'^[^0-9]+$', prompt='Please provide name and surname of recipient: ')
    file.write("Recipient's name: " + recipient_name)

    # Choice of payment method
    print('\nSelect your input number method')
    payment_method = pyip.inputMenu(['Account', 'Phone'], numbered=True)
    file.write("\nPayment method: " + payment_method)

    # Providing account or phone number
    input_number = pyip.inputNum('Plesae provide your ' + payment_method.lower() + ' number (without spaces): ')
    file.write("\n" + payment_method.title() + ': ' + str(input_number))

    # Title
    title = pyip.inputStr('Please input title of yours transfer (max lenght 50 characters: ',
                          blank = True, blockRegexes=[r'\w{51}'])
    file.write("\nTitle of transfer: " + title)

    # Currency
    currency = pyip.inputMenu(['$', 'PLN', 'EURO'], numbered=True)

    # Amount
    if currency == '$':
        amount = pyip.inputFloat('Please input amount you want to transfer: ', min=1, max=400)
    elif currency == 'PLN':
        amount = pyip.inputFloat('Please input amount you want to transfer: ', min=1, max=1000)
    elif currency == 'EURO':
        amount = pyip.inputFloat('Please input amount you want to transfer: ', min=1, max=300)
    file.write("\nAmount: " + str(amount) + ' ' + currency)

    # Date of transfer
    transfer_date = pyip.inputDate("Please provide planed date of transfer: (Accepted formats: %m/%d/%y',%m.%d.%Y)",
                                   formats = ('%m/%d/%Y', '%m.%d.%Y'))
    file.write("\nDate of transfer: " + str(transfer_date))

    # Confirmation
    confirmation = pyip.inputYesNo('Do you confirm all provided data ?')

    # Email confirmation
    if confirmation == 'yes':
        email_confirmation = pyip.inputYesNo("Money have been sent. Would you like to receive an email confirmation ?")
        if email_confirmation == 'yes':
            email = pyip.inputEmail("Please input your email:")
            file.write("\nEmail: " + email)
            print("Confirmation has been send")
        else:
            print("Thank you")
    else:
        print("Operation has been canceled")
