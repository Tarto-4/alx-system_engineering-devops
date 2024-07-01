# File Transfer Script

This Bash script automates the secure transfer of files from a client machine to a remote server using `scp`.

## Requirements

* **Operating System:** Ubuntu 16.04 LTS
* **Shellcheck:** Version 0.3.7 (or newer)
* **SSH:** OpenSSH client installed (`scp` command)
* **Private Key:** A valid SSH private key for authentication.

## Usage

```bash
./0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY

# Nginx Installation and Configuration Script

This Bash script automates the installation and basic configuration of Nginx on an Ubuntu 16.04 LTS server.

## Requirements

* **Operating System:** Ubuntu 16.04 LTS
* **Shellcheck:** Version 0.3.7 (or newer)

## Usage

1. **Copy the script:** Transfer the `1-install_nginx_web_server` script to your `web-01` server.
2. **Make it executable:** Run `chmod +x 1-install_nginx_web_server`
3. **Execute the script:** Run `./1-install_nginx_web_server`. This will:
    - Install Nginx.
    - Create a simple "Hello World!" page.
    - Test the Nginx configuration (optional).
    - Reload Nginx to apply the changes.

## Verification

1. **Local Test:** On the server itself, run `curl localhost` or `curl 127.0.0.1`. You should see "Hello World!" printed in the terminal.
2. **Remote Test:** From another machine, replace `34.198.248.145` with your server's IP address and run `curl 34.198.248.145/` or `curl -sI 34.198.248.145/` to get detailed headers.

## Additional Notes

* This script does not handle complex Nginx configurations. 
* If you run into issues, check the Nginx error logs usually located in `/var/log/nginx/error.log`.
* The `-y` flag in the `apt-get` commands automatically answers "yes" to prompts. Remove them if you prefer to confirm each step manually.
