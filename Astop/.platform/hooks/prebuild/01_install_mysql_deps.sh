#!/bin/bash
set -e

# Update metadata
dnf makecache

# Install MySQL/MariaDB client headers and build tools
dnf install -y \
    mariadb-connector-c-devel \
    gcc \
    python3-devel \
    pkgconf-pkg-config
