import json

people_string = """
{
    "people":[
    {
    "people":"Adelina Stirane",
    "phone": "22349982",
    "emails" : "ann.sti@gmail.com"
}
]}
""" 

data=json.load(people_string)
print(data)
print(data['people'])