## Natas9 - Command Injection

### Description
In current level of Natas we can see how working 'command injection', Developers of Natas show us how it works through a vulnerable input field that uses a default grep command.

### Exploit Logic
1. **Injecting the command:** We using the pipe "|" to bypass the stock command writen by developers and write our command that open for us the file where located the password to next level.
2. **Finding and printing the pass:** Script search the password uses a Re (ReGex) Library to find the password in HTTP response, specifically, the re.search() method with specified parameters.

## Results
The python script successfully inject the command into the input field and script give us a password to next level.