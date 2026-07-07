## Natas11 - Weak Encrypting Method Of Cookie.

### Description
In current level the developers of Natas show us how insecure data(specifically within a session cookie) can be exploited. Developers just encode the cookie and show us the encoded and decoded version of json, XOR encryption is weak because have a math vulnerability its like a school equation

### Exploit Logic
1. **Extract Cookie:** Script sends an HTTP GET request via library with name 'requests' and extracts the default session cookie directly from the response headers.
2. **Decode Token:** That script uses 'urllib.parse.unquote' to remove URL percentages and then 'base64.b64decode' to convert the string into raw ciphertext bytes.
3. **Recover key:** Script performs a byte-by-byte XOR ('^') between ciphertext bytes and the known default JSON string, then uses 're.search' to catch the clean 4-letter key.
4. **Forge Payload:** That script creates a modifed JSON string, encrypts it via XOR with repeating key using modulo ('%'), and encodes it back using 'base64-b64encode' and 'urllib.parse.quote'.
5. **Get Flag:** Script sends the forged cookie inside a dictionary using 'requests.get' and the uses 're.search' with unique parameters to find the 32-character password in HTML response text.

### Results
Script successfully decrypted the XOR key, forged the session cookie, and sent us a password from the HTML response.