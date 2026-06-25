## Natas4 - Weak Validation Method.

### Description
In current level we can see typical Vulnerability where validation method is weak. On this level developers using "referer" parametr in header of response for validate where are user from. This parametr very easy to spoof.

### Exploit Logic
1. **Session Initialization:** Create a persistent 'requests.Session()' object to handle connection pooling and automatically manage authentication ('session.auth').
2. **Header Configuration:** Define a headers[^1] dictionary with a custom 'referer' key set to the Natas5 URL to spoof the request origin.
3. **HTTP GET Request:** Execute a 'session.get' request to the target Natas4 URL, passing the custom headers and setting a 'timeout=5'.
4. **Response Validation:** Check if the server returns a '200 OK' status code. If successful, print the raw HTML response containing the password. Otherwise, output an error.

### Results
WebSite give us a password to next level! 

[1^] - (HTTP headers) -  requests to server where located ur user agent and other any information
