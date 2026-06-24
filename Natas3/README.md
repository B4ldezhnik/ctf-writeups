## Natas3 - Sensitive Directory Exposure

### Description
In the third level of Natas, there are no clues or passwords left in HTML source of the main page. However, the system relies on security through obscurity, leaving sensitive directories exposed via standart web files meant for search engine crawlers.

### Exploit Logic
1. **Targeting 'robots.txt'**: Web developers use a file named 'robots' in the root directory of a website to tell search engine bots which pages or folders the should not index. For a Penetration tester this file is a goldmine.
2. **Finding The Hidden Dir.:** By making a GET request to "https://natas3.natas.labs.overthewire.org/robots.txt", we can find Disallow directive pointing to a poorly hidden folder.
3. **Extracting the pass:** Navigating to that hidden directory reveals an unprotected folder structure containing a text file with the password for next level.

### Results
The automated Python script reads the 'robots.txt' file, extracts the secret path, and fetches the pass.