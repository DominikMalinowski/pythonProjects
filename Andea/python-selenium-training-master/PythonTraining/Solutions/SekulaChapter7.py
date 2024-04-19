import re  

text = 'Mark Davis MarkDavis@gmail.com Carl Jugen carl.jugen@university.edu Black Dynamite black-123-dynamite@very-explosive.pl'

#finding email  
list = re.findall('\S+@\S+', text)     
  
# printing list 
print(list)