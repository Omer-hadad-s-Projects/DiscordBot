#!/bin/bash

# Prompt the user to enter the token
read -p "Enter your Discord token, leave empty to keep the old one: " TOKEN

# Check if the token is empty
if [ -z "$TOKEN" ]; then
  echo "Empty token. Exiting..."
  exit 1
fi

sh env/env_value_saver.sh "DISCORD_TOKEN" "$TOKEN"