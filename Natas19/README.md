## Natas19 - Session Hijacking via Obfuscated Session Prediction

## Problem Statement:
The challenge requires access to the admin interface of the web application. No credentials are provided, and the application relies entirely on session state validation to determine user roles.

## Description of Vulnerability:
The Application uses weak session management where user profiles are mapped to identifiers within predictable pool (ranging from 1 to ~6400). Unlike the previous(18 Natas) level, the 'PHPSESSID' cookie is obfuscated using Hex-encoding to mask its iternal sctructure.

Crucially, session allocation is randomized rather than sequential, meaning an attacker cannot guess adjacent IDs. However, the session formatting relies on a static, insecure template: '[Session-ID]-admin' for administrative accounts. The server decodes the Hex string and executes a strict literal check ('if $username === "admin"'), bypassing database queries and renderubg typical SQL Injection string useless.

## Exploit Logic:
Since manually guessing a randomized ID across a 6400-range in inefficient, I implemented an automated Python BruteForce script using a success Oracle base on HTTP response inversion logic:

1. **Session Format Reconstruction:** The script loops through the randomized session ID range (1 to 6400) and appends the target username format ('-admin').
2. **Data Encoding:** On each iteration, the raw string (e.g., '281-admin') is converted into bytes and encoded into a HEX string to match the application's cookie format.
3. **PayLoad Injection:** The generated HEX payload is injected directly into 'PHPSESSID' cookie header of the HTTP request.
4. **Filtering responses:**
 * A Regular user session returns standard response text containing strings like 'regular user'.
 * An Admin user session returns unique text in response like printed in script

## Results:
The active administrative session ID ('cesnored') was successfully recovered. 