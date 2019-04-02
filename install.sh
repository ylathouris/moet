#!/usr/bin/env bash

# Create virtual env
printf "> Creating virtual environment for installation...\n"
rm -rf .venv
python3 -m venv .venv

# Activate env
source .venv/bin/activate

# Update pip
printf "\n> Updating pip...\n"
pip install --upgrade pip

# Install dependencies
printf "\n> Installing dependencies...\n"
pip install .

printf "\n> Done!\n"
