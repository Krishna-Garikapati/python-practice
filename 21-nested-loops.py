# Print
# 1 2 3
# 1 2 3
# 1 2 3
for i in range(3):
    for j in range(1):
        print("1 2 3")

#print
# *****
# *****
# *****
for i in range(3):
    for j in range(1):
        print("*****")

#print
# 1
# 12
# 123
# 1234
for i in range(1,5):
    for j in range(1,i+1):
        print(j, end="")
    print()