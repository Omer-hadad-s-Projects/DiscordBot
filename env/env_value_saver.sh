KEY=$1
VALUE=$2

if [ -z "$VALUE" ]; then
    echo "Empty value. Exiting..."
    exit 1
fi

# Construct the path for the .env file in the parent directory
ENV_FILE=".env"

# Check if the .env file exists
if [ ! -f "$ENV_FILE" ]; then
    echo ".env file not found! Creating a new one."
    touch "$ENV_FILE"
fi

# Add or update the key-value pair in the .env file
if grep -q "^$KEY=" "$ENV_FILE"; then
    # Update the existing key
    sed -i.bak "s/^$KEY=.*/$KEY=$VALUE/" "$ENV_FILE"
else
    # Add the new key
    echo "$KEY=$VALUE" >>"$ENV_FILE"
fi

echo "Saved $KEY=$VALUE to $ENV_FILE"
