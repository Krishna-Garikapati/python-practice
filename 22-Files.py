#Q1. Create & Write Using Variables
#only practicing modern way using with...: function to avoid using close() function at end
filename = "students.txt"
#myFile is just a variable name that represents the opened file.
#creating a file and giving write access
with open(filename, "w") as myFile:
    myFile.write("line1\n")
    myFile.write("line2\n")
    myFile.write("line3\n")

#Q2. Read Full File
#f is just a variable name that represents the opened file.
with open(filename,"r") as f:
    #lets read the file
    data = f.read()
    #print contents of file
    print(data)

#Q3. Append Data
#Add "Mike" to the file.
with open(filename,"a") as f:
    f.write("line4\n")

#Q4. Read 1st line of file
with open(filename,"r") as f:
    data=f.readline()
    print(data)

#Q5. Count Lines
count=0
with open(filename,"r") as f:
    for line in f:
        count=count+1
print(count)

#Q6. Search for a Name
with open(filename,"r") as f:
    data=f.read()
    if "line1" in data:
        print("found")
    else:
        print("not found")
