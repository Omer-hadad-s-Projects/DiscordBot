KEY=$1
VALUE=$2

if [ -z "$VALUE" ]; then
    echo "Empty value. Exiting..."
    exit 1
fi

ENV_FILE="env/.env"
TEMP_FILE=$(mktemp)

if [ ! -f "$ENV_FILE" ]; then
    echo ".env file not found! Creating a new one."
    touch "$ENV_FILE"
fi

if grep -q "^$KEY=" "$ENV_FILE"; then
    sed "s/^$KEY=.*/$KEY=$VALUE/" "$ENV_FILE" > "$TEMP_FILE"
else
    cp "$ENV_FILE" "$TEMP_FILE"
    echo "$KEY=$VALUE" >> "$TEMP_FILE"
fi

mv "$TEMP_FILE" "$ENV_FILE"

echo "Saved $KEY=$VALUE to $ENV_FILE"