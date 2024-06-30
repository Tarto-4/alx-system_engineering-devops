# SSH Configuration and Key Management

This project focuses on SSH configuration and key management for secure, passwordless authentication to remote servers.

## Scripts

* `0-use_a_private_key`: Connects to a server using a private key (~/.ssh/school) as the user ubuntu.
* `1-create_ssh_key_pair`: Creates an RSA key pair with a specified name, bit size, and passphrase.
* `2-ssh_config`: Contains SSH client configuration to use a private key and disable password authentication.

## Requirements

* **Operating System:** Ubuntu 20.04 LTS
* **SSH:** OpenSSH client installed
* **Private Key:** A private key file (`~/.ssh/school`) for authentication.

## Usage

1. **Make scripts executable:**
   ```bash
   chmod +x *.sh
