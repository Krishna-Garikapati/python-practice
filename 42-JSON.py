import json
json_data = '{"name": "Krishna", "age": 22, "is_student": true}'
python_data = {
    "name": "Krishna",
    "age": 22,
    "is_student": True
}
covert_to_python = json.loads(json_data)
print(covert_to_python)
print(type(covert_to_python))

convert_to_json = json.dumps(python_data)
print(convert_to_json)
print(type(convert_to_json))

# JSON is a text format. In Python, JSON data is stored as a string.
# json.dumps() converts Python objects to a JSON string, and json.loads() converts JSON string back to Python objects.