import requests

#endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
#http request
get_response = requests.get(endpoint, json={"query":"test"})
#print(get_response.text)
#print(get_response.json())
print(get_response.status_code)