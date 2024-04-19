
# loading and displaying file content 
import csv 
csvFile = open('example.csv')
csvReader = csv.reader(csvFile)
csvDataList = list(csvReader)
print(csvDataList)
csvFile.close()

# loop for displaying file content 
import csv 
csvFile = open('example.csv')
csvReader = csv.reader(csvFile)

for row in csvReader:
    print( 'Row # '+ str(csvReader.line_num) + str(row))
csvFile.close()

# adding data to file 
import csv 
csvFile = open('example2.csv','w', newline='')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['10.11.2023  21:37:01, apple, 420'])
csvWriter.writerow(['11.11.2023  21:37:02, pen, 69'])
csvWriter.writerow(['12.11.2023  21:37:03, pineapple, 2137'])
csvFile.close()

# tab separated values 
import csv 
csvFile = open('example2.csv','w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['10.11.2023  21:37:01', 'apple', '420'])
csvFile.close()
