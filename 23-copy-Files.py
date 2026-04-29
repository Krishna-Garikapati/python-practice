# Q7. Copy File
# 👉 Copy students.txt → backup.txt.

filename1="students.txt"
filename2="backup.txt"
with open(filename1,"r") as f1:
   data=f1.read()

with open(filename2,"w") as f2:
   f2.write(data)