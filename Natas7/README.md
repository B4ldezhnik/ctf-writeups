## Natas7 - Local File Inclusion

### Description
In current level the website includes a file based on the value of 'page' parametr, but developer didn't validate this input.

### Exploit Logic
1. **Connecting:** The script sets up the target URL and HTTP Basic Auth credentials.
2. **Crafting the payload:** Instead of a legitmate page name, the script sets the 'page' parameter to an absolute path '/etc/natas_webpass/natas8'.
3. **Sending the request:** The script sends a GET request with this crafted parameter, exploiting the lack of input validation in the server's 'include()' call.
4. **Results extraction:** The server includes the contents of the requested file directly into the page, and the script prints the full response, which contains the password to next level.

### Results
The script successfully retrieved the password to us!