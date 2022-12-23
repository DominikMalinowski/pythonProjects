def Chapter3(length, spccount, numcount, excludedcharacters): 
#first is the overall length of the password, second is special character count
#third is number character count and last one is a list of excluded characters
#which will not appear in generated password
    import random #module for randomize function
    import string #module for string function
    import string_utils as su #module for string shuffling
    x = 1 #string for while loops
    password = "" #password assignment (empty string)
    charcount = length - spccount - numcount #extracting number of letter characters
    while x <= charcount: #first loop for letter (uppercase and lowercase)
        char = random.choice(string.ascii_letters) #assigning first value to char variable
        while char in excludedcharacters: #while loop for excluding characters provided on input
            char = random.choice(string.ascii_letters) #Program will randomize value until it will be outside the group of the excluded characters
        password = password + char #concatenation of character
        x += 1 #incrementation of value for while loop
    x = 1 #resetting value to initial state - will be used in the next while loop
    while x <= spccount: #second loop for special characters
        char = random.choice(string.punctuation)
        while char in excludedcharacters:
            char = random.choice(string.punctuation)
        password = password + char
        x += 1
    x = 1
    while x <= numcount: #third loop for number characters
        char = random.choice(string.digits)
        while char in excludedcharacters:
            char = random.choice(string.digits)
        password = password + char
        x += 1
    password = su.shuffle(password) #shuffle order of characters in string
    return password #return password

print(Chapter3(15,5,5,"123456789qwertyuiopasdfghjklzxcvbn"))