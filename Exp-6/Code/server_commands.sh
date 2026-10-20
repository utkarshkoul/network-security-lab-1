#!/bin/bash

# Run these commands on the Ubuntu server.

# Install OpenSSH Server if it is not already installed.
sudo apt update
sudo apt install openssh-server

# Start and enable the SSH service.
sudo systemctl enable --now ssh

# Check service status and confirm that SSH is listening on TCP port 22.
systemctl status ssh --no-pager
sudo ss -tlnp | grep ':22'

# Record server identity details for the client-side connection.
whoami
hostname
hostname -I
sudo ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub