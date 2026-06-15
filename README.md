# Natas16 - Blind command injection Writeup

## Problem Statement
The challenge required extracting the password for "Natas17" from a file located at '/etc/natas_webpass/natas17'. The web application uses 'grep' to filter a dictionary file based on user input, but in filter out common injection symbols like ";/\" and "&"

## Vulnerability Analysis
The application is vulnerable to command injection via the Bash '$(...)'  subshell execution. By injecting a subshell, we can execute arbitrary commands despite the input filters.

## Exploit logic
Since the application output is not directly reflected (Blind Injection), I implemented an automated script that uses a **Success Oracle** based on the HTTP response body length:
1. **Validation Trigger**: The script iterates through a character set.
2. **Side-Channel Analysis**: It measures the length of the HTTP response using Python's "len()" function.
3. **Filtering**
	- An incorrect characters returns an 1122-byte responce.
	- A correct characters returns an 1105-byte responce <-  this a valid character

##Results
The password was successfully recovered by automating this request loop, demonstrating the effectiveness of blind injection techniques in bypassing restricted command shells
