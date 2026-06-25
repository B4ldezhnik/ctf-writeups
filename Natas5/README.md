## Natas5 - Weak Authentication.

### Description
The application uses a client-side HTTP cookie named 'loggedin' to check the user's authentication status. If the cookie is '0', the server assumes the user is not logged in. Since cookies are stored on the client side, the can be easily spoofed to bypass authentication.

### Exploit Logic
1. **Target Setup:** Define the target URL for Natas5 and pass the HTTP Basic Authentication credentials 'auth' retrieved from previous level.
2. **Cookie Forgery:** Create a custom dictionary 'my_cookie' with a key 'loggedin' set to '1' to spoof an authenticated session state.
3. **HTTP GET Request:** Use 'requests.get()' to send a intentional pause in execution for synchronization and stability.
4. **Response Validation:** Convert the server responseto lowercase using 'lower()' and check if the substring 'access granted' is present. This ensures robust string  matching regardless of case.

### Results
The script successfully bypased the authentification method of website and gives us a password for next level.