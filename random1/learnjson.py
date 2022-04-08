# write into the json file
import json

employee = {
    "name": "sudhir singh",
    "age": 32,
    "city": "Bangalore",
    "company": "Cloudera"
}

with open("data.json", "w") as write_file:
    json.dump(employee, write_file)

json_string = json.dumps(employee)
print(type(json_string))
print(json_string)

with open("data.json", "r") as reader_file:
    b = json.load(reader_file)
    print(type(b))
    print(b)

b = json.dumps(employee)
print(type(b))
print(b)

y = json.loads(b)
print(type(y))
print(y)
