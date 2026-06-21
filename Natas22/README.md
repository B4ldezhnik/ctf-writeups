## Natas22 - EAR[^1]

## Description
This level have a critical logical flaw in webpage knwon as **"EAR"**.

The developer utilized the "header("location: /")" Function to redirect unauthorized users but forgot to terminate the script. As a result, when a valid GET parameter is supplied, the server continues executing the underlying code, generates the secret content(flag), and appends it to the response body.

Standard web browsers obediently follow the "Location" header and hide the response body from the user. However. the raw HTTP response still contains the sensitive data.

---

## Exploitation Logic
1. **Pipeline Analysis:** Passing the Get parameter '?revelio=1' forces the server to enter the target 'if' condition.
2. **Bypassing the Redirect:** Since the script execution doesn't halt, the flag is generated into the response body anyway.
3. **Data Interception:** Using a Python script with 'allow_redirects=False' prevents the client from following the redirect, allowing us to capture in its raw form directly from the response body.

---

## Results
Script give us a key to Natas23.


[^1] - Execution After Redirect