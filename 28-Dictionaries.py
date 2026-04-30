# Q4. largest number
data = {"a": 5, "b": 15, "c": 20}
print(data.values())
data_values = data.values() #[5,15,20]

result=0
for i in data_values:
    if i>result:
        result=i
print(result)

# Copy Dictionaries
new_data=data.copy()
print(new_data)
new_data["d"]=30
new_data["a"]=10
print(new_data)