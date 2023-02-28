import json

people_string = '''

{
    "people": [
      {
      
        "name": "John Smith",
        "phone": "615-555-7164",
        "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
        "has_license": false
      
      },
    
    {
        "name": "Jane Doe",
        "phone": "560-555-5133",
        "emails": [null],
        "has_license": true
      
    }
    
    ]

}


'''

data=json.loads(people_string)

print(type(data['people']))
for person in data['people']:
  del person['phone']

new_string=json.dumps(data)

print(new_string)
