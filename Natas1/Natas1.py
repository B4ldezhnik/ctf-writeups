import requests

url = "http://natas1.natas.labs.overthewire.org/"
auth = ("natas1", "secret")

response = requests.get(url, auth=auth)

print("Here is your password in response:")
print(response.text)