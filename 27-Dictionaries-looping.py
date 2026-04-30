#loops
# Q1. Print all keys and values

event = {
    "FavColor":"Orange",
    "FavFlower":"Tuplips",
    "Theme":"Animal",
    "Age":"27"
}

print(event.items())

for i,j in event.items():
    print(i)
    print(j)

# Q3. Print key and value
    print(f"Key is {i} and value is {j}")