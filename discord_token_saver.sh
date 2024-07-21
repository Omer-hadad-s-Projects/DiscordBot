#!/bin/bash

# Prompt the user to enter the token
read -p "Enter your Discord token, leave empty to keep the old one: " TOKEN

# Check if the token is empty
if [ -z "$TOKEN" ]; then
  echo "Empty token. Exiting..."
  exit 1
fi

# Define the .env file
ENV_FILE=".env"

# Check if .env file exists
if [ ! -f $ENV_FILE ]; then
  touch $ENV_FILE
fi

# Update or add the DISCORD_TOKEN line in the .env file
if grep -q "DISCORD_TOKEN=" $ENV_FILE; then
  # Replace the line if it exists
  if [ "$(uname)" == "Darwin" ]; then
    # macOS (BSD sed)
    sed -i '' "s/^DISCORD_TOKEN=.*/DISCORD_TOKEN=$TOKEN/" $ENV_FILE
  else
    # Linux (GNU sed)
    sed -i "s/^DISCORD_TOKEN=.*/DISCORD_TOKEN=$TOKEN/" $ENV_FILE
  fi
else
  # Add the line if it doesn't exist
  echo "DISCORD_TOKEN=$TOKEN" >> $ENV_FILE
fi

echo "Token saved to .env file"
