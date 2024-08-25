# Web Stack Debugging - High Concurrency Nginx Configuration

## Project Overview

This project involves debugging and optimizing an Nginx web server configuration to handle a high number of concurrent HTTP requests efficiently. The goal is to eliminate failed requests during benchmarking with ApacheBench, ensuring the server can manage a significant load without errors.

### ApacheBench Benchmarking Results

- **Initial Test**: The server failed 943 requests out of 2000 due to inadequate configuration for handling high concurrency.
- **Final Test**: After applying the Puppet manifest, the server successfully handled all 2000 requests with 0 failed requests.

### Files

- **0-the_sky_is_the_limit_not.pp**: This is the Puppet manifest that configures Nginx to handle high concurrency. The configuration includes:
  - Automatically setting the number of worker processes based on available CPU cores.
  - Increasing the number of worker connections.
  - Optimizing buffer sizes and timeouts for better performance under load.

- **nginx.conf.erb**: A template file for the Nginx configuration, used by the Puppet manifest.

### Requirements

- Ubuntu 14.04 LTS
- Puppet v3.4
- Puppet-lint v2.1.1

### Setup and Usage

1. **Install Nginx** (if not already installed):
   ```bash
   apt-get update
   apt-get install -y nginx
