## Natas18 - Session Hijacking via Session ID Brute-Force.

## Problem Statement:
The challenge requires accessing the administrative interface of the web application. However, no credentials are provided, and the application relies on session management to determine user privileges.

## Description of Vulnerability:
The application uses weak, sequential session identifiers ('PHPSESSID') ranging from 1 to 640.
Because the session IDs are predictable and the application doesn't re-verify user credentials after the session is created, an attacker can brute-force the active session IDs to hijack an admin session.

## Exploit logic
Since manually guessing the correct Session ID is inefficient, I implemented an automated Python BruteForce script using a Success Oracle based on HTTP response body content:

1. **Validation Trigger:** The script loops through the predictable session ID range (1 to 640).
2. **Session Injection:** On each iteration, the integer is injected into the 'PHPSESSID' cookie header.
3. **Side Channel Analysis:** The script converts the returned HTTP response text to lowercase using Python's
4. **Filtering:**
 * A Regular user session returned in response text standard page content.
 * A Admin user session returned in response unique page content.

## Results:
The administrative session ID was successfully recovered by automated Python script
