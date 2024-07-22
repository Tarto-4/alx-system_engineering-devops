# Setting up ufw Firewall on web-01

This repository contains a bash script (setup_firewall.sh) that automates the configuration of the ufw firewall on web-01 server. The script ensures that only essential incoming TCP ports (22 for SSH, 443 for HTTPS, and 80 for HTTP) are allowed, while blocking all other incoming traffic.
Requirements

    Server: web-01
    Software: ufw (Uncomplicated Firewall)

Usage

    Clone the Repository: Clone this repository onto your web-01 server.

    bash

git clone https://github.com/your-username/alx-system_engineering-devops.git

Navigate to the Directory: Go to the directory containing the firewall setup script.

bash

cd alx-system_engineering-devops/0x13-firewall

Make the Script Executable: Ensure that the bash script has execute permissions.

bash

chmod +x setup_firewall.sh

Run the Script: Execute the script with root privileges to set up the ufw firewall.

bash

sudo ./setup_firewall.sh

Verify ufw Status: After running the script, verify the ufw status to ensure the rules are applied correctly.

bash

    sudo ufw status verbose

Explanation

The setup_firewall.sh script performs the following actions:

    Checks if the script is run as root.
    Installs ufw if it's not already installed.
    Resets ufw to default settings (ufw --force reset).
    Configures ufw to deny all incoming traffic by default (ufw default deny incoming).
    Allows incoming TCP traffic on ports 22 (SSH), 443 (HTTPS), and 80 (HTTP) (ufw allow <port>/tcp).
    Enables ufw with the new rules (ufw --force enable).
    Displays the verbose status of ufw to confirm the applied rules (ufw status verbose).

This setup enhances security by restricting incoming connections to only essential services, reducing the attack surface of the web-01 server.