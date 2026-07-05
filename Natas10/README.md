## Natas10 - Command Injection in more stringent environments.

### Description
In current level we can see how Developers of Natas trying to "patch" vulnerability, but they just block basic specific symbols, but forget to block more unique symbols like "&$."

### Exploit Logic
1. **Sending the post request:** We using the 'Requests' Library to send a POST request in this website and in this input field with name 'needle' exactly, we using one function of this library: 'requests.post' with unique settings, where data(this is what we can write in input field) is our exploit command.
2. **Searching the password in response:** In this script searching of password in reponse doing the function 're.search' of library ReGex with unique parameters (32 letters and A-Za-z0-9 symbols in word(password)).

### Results
Script successfully send request and get the response where he search the password to next level.