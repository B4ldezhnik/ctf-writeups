## Natas8 - Encoded Pass-Code.

### Description
On this level of Natas Developers show us how the Encoding work, he show to us this uses a Base64 and HEX encoding.

### Exploit Logic
1. **Searching Encoded Pass-code:** Script uses a 're.search' tool with unique parameters(a-f0-9 and 32 letters in word) to find the pass-code.
2. **Decoding Pass-Code:** That script uses a base64 library to decode a secret pass-code.
3. **Searching and sending password to me:** The script searching password with 're.search' tool with unique parameters, after this password sending to us.

### Results
Script successfull decoded secret and send us a password from GET response