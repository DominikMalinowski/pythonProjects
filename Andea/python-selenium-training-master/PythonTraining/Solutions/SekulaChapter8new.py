import pyinputplus as p

name = p.inputStr("Enter first name: ", blockRegexes=[r'[\d\W]'])
payment = p.inputMenu(("Account number", "Phone number"), "Select payment method:\n"
                                                          "1. Account number\n"
                                                          "2. Phone number\n", numbered=True)
if payment =="Account number":
    accountNum = p.inputStr("You have chosen the account number. Enter account number: ", blockRegexes=[r'\D'])
else:
    phoneNum = p.inputNum("you have chosen the phone number. Enter phone number: ")

title = p.inputStr("Enter title name: ", blank=True, blockRegexes=[r'\w{50}'])
currency = p.inputMenu(("Dolar", "EURO", "PLN"), "Select currency:\n"
                                                 "1.Dolar\n"
                                                 "2.EURO\n"
                                                 "3. PLN\n"
                                                 "", numbered=True)
if currency == "Dolar":
    amount = p.inputFloat("You have chosen Dolar. Enter transfer amount: ", min=1, max=400)
elif currency == "EURO":
    amount = p.inputFloat("You have chosen EURO. Enter transfer amount: ", min=1, max=300)
else:
    amount = p.inputFloat("You have chosen PLN. Enter transfer amount: ", min=1, max=1000)

transferDate = p.inputDate("Enter date of transfer:", ("%d.%m.%y", "%m.%d.%Y", "%m.%d.%y", "%Y.%m.%d", "%y.%m.%d"))
confimation = p.inputYesNo("Would you like to confirm operation? (yes/no): ")
if confimation == "yes":
    confimationEmail = p.inputYesNo("Operation has been confirmed. Would you like to receive confirmation email? (yes/no): ")
    if confimationEmail=="yes":
        email = p.inputEmail("Enter email: ")
        print("Email has been sent.")
else:
    print("Operation has not been confirmed.")
