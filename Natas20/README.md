## Natas20 - Session Injection

## Description:
This exploit automates the process of bypassing browser formatting restrictions and manipulating custom backend session management mechanism to gain administrative privilegges.

---

## Vulnerability Analysis:

### The problem of Natas20
The target application utilizes a custom session handler ('mywrite' / 'myread') that stores session variables flatly in text files on server's disk. Each variable is stored in a `key value` format, separated by a newline character '\n'.

Because the application fails to sanitize or validate the user-supplied 'name' parameter before writing it to the session file, it is vulnerable to **Session Injection**.

### Exploitation Mechanism:
1. **First Phase (Post Request):** The script sends a payload via the 'name' field containing an encoded newline character: 'Mike\nadmin 1'. The server process executes 'mywrite()' and writes the raw input into the session file. The embedded newline forces the underlying text file sctructure to split, injecting 'admin 1' onto a brand new line.
2. **Second Phase (Get Request):** The script issues a follow-up request preserving the session cookie 'PHPSESSID'. The backend executes 'myread()', parsing the session file line-by-line. It reads 'admin 1' as a separate, legitimate session variable, granting admin access and exposing the flag.
 
