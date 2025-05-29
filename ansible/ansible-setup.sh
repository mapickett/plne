#!/usr/bin/bash

# Install required packages
pip install -r requirements.txt

# Create required directories
mkdir collections

# Install required collections
ansible-galaxy collection install -r requirements.yml

# Test connectivity
ansible all -m ping