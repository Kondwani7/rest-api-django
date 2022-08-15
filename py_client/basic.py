import requests

#endpoint = "https://httpbin.org/status/200/"
endpoint = "http://localhost:8000/api"
#http request
get_response = requests.get(endpoint, json={"query":"test"})
#print(get_response.text)
print(get_response.json()['message'])
#print(get_response.status_code)