## Natas12 - Default **RCE**[^1]

### Description
In level 12 of Natas developers show us how RCE(Remote Code Execution) works. Simply put, this vulnerability is caused by poor input validation or a complete lack of filtering in the file upload script on the server side. As a result, we can upload any file, including malicous code, which the server will then execute.

### Exploit Logic
1. **Creating File:** Script creating a table with name 'files' where the 'uploadfile' variable is located and value of it 'anything.php' - file with malicous code.
2. **Extension Spoofing:** The script in 'data' forcing the script to upload the file with php extension using a server's variable 'filename' with name of file and PHP extension.
3. **Searching the path:** Script using a re.search function with unique parameters to find the path of file that script created.

### Results
Script successfully spoofed the extension of malicous file that it created.

[^1]: Remote Code Execution - https://www.geeksforgeeks.org/computer-networks/what-is-remote-code-execution-rce/ 
