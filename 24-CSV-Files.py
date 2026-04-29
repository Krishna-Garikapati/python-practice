# i am using a csv file thats provided in class example:
#Q8. CSV Read
#Read a CSV file and print rows.

import csv
filename="Monster Spreadsheet (D&D5e) - Official Stats.csv"
 
with open(filename,"r") as f:
    data=csv.reader(f)
    for line in data:
        print(line)
        #print 1st column of all rows
        print(line[0])