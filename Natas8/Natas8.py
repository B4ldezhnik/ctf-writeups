import requests
import base64
import re
import sys
import time

url = "http://natas8.natas.labs.overthewire.org/"
auth = ("natas8", "secret")

enc_sec = ""

print("[*]Connecting . . .")

time.sleep(1)

ses_get = requests.get(url=url + "index-source.html", auth=auth)
flag = re.search(r"([a-f0-9]{32})", ses_get.text, re.IGNORECASE)

if flag:
    enc_sec += flag.group(1)
    print("[+]Encoded Secret was founded!")
else:
    sys.exit("[-]Secret word was not finded in response.")

decode1 = bytes.fromhex(enc_sec)
decode2 = decode1[::-1] # This line writes the secret in reverse
decode_final = base64.b64decode(decode2).decode('utf-8')

payload = {
    "secret": decode_final,
    "submit": "Submit"
}

time.sleep(0.5)

print(f"[+]Your secret(not password!): {decode_final}")

ses_post = requests.post(url=url, data=payload, auth=auth)

print("[+]Successfully! your password here!:")

flag2 = re.search(r'for natas9 is ([A-Za-z0-9]{32})', ses_post.text, re.IGNORECASE)

print(flag2.group(1))