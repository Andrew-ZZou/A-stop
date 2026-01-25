#!/bin/bash

# Install dependencies for mysqlclient on Amazon Linux 2023
sudo dnf install -y mariadb-connector-c-devel gcc python3-devel

set -e

# Update metadata
dnf makecache

# Install MySQL/MariaDB client headers and build tools
dnf install -y \
    mariadb-connector-c-devel \
    gcc \
    python3-devel \
    pkgconf-pkg-config
