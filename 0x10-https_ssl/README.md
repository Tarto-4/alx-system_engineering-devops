This script, `0-world_wide_web`, is designed to provide information about DNS records associated with specific subdomains within a given domain. It uses the `dig` command to query DNS servers and `awk` to process the output, extracting the record type (e.g., A, CNAME) and the destination IP address.

The script is flexible and can handle the following scenarios:

- **Domain Only:** If you provide only the domain name as an argument, the script will display information for the subdomains `www`, `lb-01`, `web-01`, and `web-02`.
- **Domain and Subdomain:** If you provide both the domain name and a specific subdomain, the script will display information only for that subdomain.

**Prerequisites:**

- The script assumes that you have `dig` and `awk` installed on your system. These are standard tools on most Unix-like systems.

**Example Usage:**

```bash
./0-world_wide_web example.com          # Display info for all default subdomains
./0-world_wide_web example.com web-01  # Display info for the web-01 subdomain




**How it works:**

1. **Shebang:**  The first line ensures the script is run with Bash.
2. **Comment:** The second line explains the script's purpose.
3. **`get_record_info` Function:**
   - Takes a subdomain as input.
   - Uses `dig +short` to get a concise output of DNS records.
   - Employs `awk` to split the output by spaces and extract the first field (record type) and last field (destination).
4. **`main` Function:**
   - Takes the domain and optional subdomain as arguments.
   - Sets a default list of subdomains if none is provided.
   - Iterates through each subdomain:
     - Calls `get_record_info` to get record details.
     - Checks if the information is valid.
     - Prints a formatted message with the subdomain, record type, and destination.
5. **Script Execution:**
   - The `if` statement ensures the `main` function is called only when the script is run directly (not sourced).



**Key improvements:**

*   The script adheres to the given requirements and best practices.
*   The `get_record_info` function improves modularity and readability.
*   Clear comments are included for better understanding.
