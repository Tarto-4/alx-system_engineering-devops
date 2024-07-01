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
