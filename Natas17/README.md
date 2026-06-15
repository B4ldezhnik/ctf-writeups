# Natas17 - Time Based Blind injection WriteUp

## Problem Statement
The Web Page looks completely identical regardless of whether our input is true or false.
Standard blind injection (boolean-based) doesn't work here because there is no visual difference in server response.

## Methodology
**The strategy**:
If we cannot see any visual changes in response, we use the "SLEEP()" to force the database to delay its response when a correct character is found.
**Case Sensitivity**:
My SQL text comparison is case-insensitive by default.
To accurately crack the password (which contains both uppercase and lowercase letters), we must use the "BINARY" operator directly before the character variable.

## Results
**Final Output**:
The script automatically extracts the 32-character password bit by bit in just a few minutes