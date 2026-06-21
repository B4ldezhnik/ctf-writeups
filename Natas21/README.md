## Natas21 - Session Poisoning

## Description:
This exploit automates the process of poisoning the current PHP session with injecting the flag into POST request body on expirement subdomain, its giving us admin privelegies BUT only in main webpage that colocated with expirement webpage.

## How it Works
1. **Vulnerability:** The expirement website takes any arbitrary POST parametrs and dumps them directly into the current PHP session container "$_SESSION" without validation.
2. **Poisoning:** The script sends a POST request to the expirement domain[^1] with the flag "admin = 1". The server processes this and saves "admin => 1" into the session file bound to our "PHPSESSID".
3. **Exploitation:** The script extracts the poisoned "PHPSESSID"[^2] cookie and reuse it to make a GET request to the main website[^3]. The main site reads the modified session, detect admin flag, and gives you credentials for next level.

## Requirements
Library "Requests"[^4]

[^1]: http://natas21-experimenter.natas.labs.overthewire.org/
[^2]: Cookie container where located ur session ID
[^3]: http://natas21.natas.labs.overthewire.org/
[^4]: https://pypi.org/project/requests/