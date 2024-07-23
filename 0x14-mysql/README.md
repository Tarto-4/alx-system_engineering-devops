# 0x14-mysql

This repository contains scripts and configurations related to setting up MySQL servers and managing MySQL databases.

## Project Overview

This project focuses on configuring MySQL servers, setting up replication between primary and replica servers, creating users, and performing backups. Each task is designed to ensure proper installation, configuration, and maintenance of MySQL databases.

## Tasks Overview

### Task 0: Install MySQL

Script: `0-install_mysql.sh`

Install MySQL 5.7.x on Ubuntu 16.04 servers.

### Task 1: Create MySQL user for checker

Script: `1-let_us_in.sql`

Create MySQL user `holberton_user` with necessary permissions for replication checking.

### Task 2: Create a database and table with data

Script: `2-if_only_you_could_see.sql`

Create database `tyrell_corp`, table `nexus6`, and insert sample data. Grant permissions to `holberton_user`.

### Task 3: Create a replica user

Script: `3-quite_an_experience.sql`

Create MySQL user `replica_user` for replication purposes.

### Task 4: Setup Primary-Replica infrastructure using MySQL

Configuration Files:
- `4-mysql_configuration_primary`
- `4-mysql_configuration_replica`

Configure MySQL primary on `web-01` and replica on `web-02`. Set up replication for database `tyrell_corp`.

### Task 5: MySQL backup

Script: `5-mysql_backup.sh`

Script to generate MySQL dump, compress it, and store as a backup.

## Repository Structure

