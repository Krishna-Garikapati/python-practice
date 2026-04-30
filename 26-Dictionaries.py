# Q5. Remove Item
event = {
    "FavColor":"Orange",
    "FavFlower":"Tuplips",
    "Theme":"Animal",
    "Age":"27"
}

event.pop("Age")
print(event)

# Q6. Loop Through Dictionary
for key, value in event.items():
    print(key, value)


# Q7. Check if Key Exists
if "Theme" in event:
    print("exists")

# type()
print(type(event))

