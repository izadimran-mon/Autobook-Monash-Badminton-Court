import requests, json

# session = requests.Session()
# print(session.__str__())
# r = requests.get('https://fmu-rbs.monash.edu.my/book/venue/6?start=2019-09-23T00%3A00%3A00&end=2019-09-30T00%3A00%3A00&_=1569240112569')
# data = r.text
# print(data)
# print(r)

response = requests.get('https://fmu-rbs.monash.edu.my/book/venue/6')
json_value = response.text
print(json_value)