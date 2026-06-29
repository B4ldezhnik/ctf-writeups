## Natas6 - Secret File With Password In Client-Visible Source.

### Description
In current level developer tried to hide a file with Pass-Code that was needed to get the password for the next level, but he wrote the path to this file in sourcecode that visible for everyone.


### Exploit Logic
1. **Connecting:** Script uses the 'Requests.session()' for connect to server, session can save cookie and other data like browser page.
2. **Finding a pass-code:** Our python script uses a 're.search' with a pattern that matches the format of this password.
3. **Using key in main website:** Script sends a POST request to the server with extracted pass-code as form data.
4. **Finding a password:** After our POST request server gave to script the response text with password inside, script with 're.search' searching valid word with 32 letters.

### Results
Script successfully written the Pass-Code into main website and it gave password to us