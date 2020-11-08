import requests
import json

'''
body = json.dumps({ "deviceid": "Device1" , "Type": "Tomato" , "Quantity": "5" , "Calories" : "10" ,  "Protein" : "12" , "Fat": "22" , "Carbs" : "22" ,  "Sugar" : "55" , "Sodium": "12" ,  "Vitamin_C": "15" ,  "Start_Date": "2016-07-02" , "End_Date": "2016-07-08" })
r = requests.post('https://refrigeratoreye.azurewebsites.net/tables/foodmanager?zumo-api-version=2.0.0' , data = body)
print r.status_code
print body
'''

'''
body = json.dumps({
"id": "901f517f-1100-4808-857c-12e900619d0c" ,
"Type": "ahmed"
})
r = requests.patch('https://refrigeratoreye.azurewebsites.net/tables/foodmanager?zumo-api-version=2.0.0', data=body)
print r.status_code
'''

'''
delete = '431d85c0-4804-4949-928e-c1932000963e'
r = requests.delete('https://refrigeratoreye.azurewebsites.net/tables/foodmanager/' + delete + '?zumo-api-version=2.0.0')
print r.status_code
'''

'''
r = requests.get('https://refrigeratoreye.azurewebsites.net/tables/foodmanager?zumo-api-version=2.0.0')
a = r.json()
b = len(a)
for i in range(0,b):
    c = a[i]
    d = c['id']
    e = d.encode("utf-8")
    print e
    print type(e)
'''
