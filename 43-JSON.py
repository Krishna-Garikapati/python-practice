# Convert this JSON into Python and print the city: '{"city": "Halifax", "province": "NS"}'
import json
json_data = '{"city": "Halifax", "province": "NS"}'
python_data=json.loads(json_data)
print(python_data)
print(python_data["city"])

# Convert this Python dictionary into JSON:
#formatting json
student = {
    "name": "Alex",
    "marks": [80, 90, 85]
}
json_data1 = json.dumps(student, indent=4, separators=(";","="))
print(json_data1)