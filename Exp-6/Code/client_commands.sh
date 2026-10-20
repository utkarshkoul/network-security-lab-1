#!/bin/bash

# Run these commands section by section on the Kali client.
# Replace both values before connecting to your Ubuntu server.
SSH_USER="your-ubuntu-user"
SSH_HOST="your-ubuntu-ip"

# Check the installed SSH client.
ssh -V

# Password-based login. Verify the host-key fingerprint before accepting it.
ssh "$SSH_USER@$SSH_HOST"

# Run inside the remote shell, then return to Kali with: exit
whoami
hostname
pwd

# Generate an Ed25519 key pair and inspect its public-key fingerprint.
ssh-keygen -t ed25519 -C "student@lab"
ls -l ~/.ssh/id_ed25519*
ssh-keygen -lf ~/.ssh/id_ed25519.pub

# Keep the private key local and restrict its permissions.
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519

# Copy the public key to the Ubuntu account.
ssh-copy-id -i ~/.ssh/id_ed25519.pub "$SSH_USER@$SSH_HOST"

# Test public-key authentication without password fallback.
ssh -o PreferredAuthentications=publickey -o PasswordAuthentication=no "$SSH_USER@$SSH_HOST"

# Optional: load the private key into an SSH agent for subsequent connections.
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh "$SSH_USER@$SSH_HOST"