#with open('pliki_tekstowe/pi_digits.txt') as file_object: 
#    contents= file_object.read() 
#print(contents.rstrip()) 

#file_path = 'C:\\projekty_python\\inne_pliki\\pliki_tekstowe\\pi_digits.txt' 
#with open (file_path) as file_object: 
#    print(file_object)

filename = 'pliki_tekstowe/pi_digits.txt' 
with open (filename) as file_object:
    for line in file_object:
        print(line.rstrip())