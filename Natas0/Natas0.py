import requests

url = "http://natas0.natas.labs.overthewire.org/"
auth = ("natas0", "natas0")

response = requests.get(url, auth=auth)

print("Here is your password in response:")
print(response.text)