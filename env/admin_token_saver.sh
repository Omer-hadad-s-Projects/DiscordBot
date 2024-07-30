read -p "Enter your admin tokens seprated by ',' leave empty to keep unchanged: " VALUE

if [ -z "$VALUE" ]; then
    echo "Empty admin list, skipping..."
    exit 1
fi

WRAPPED_VALUE="[$VALUE]"

sh env/env_value_saver.sh "ADMIN_LIST" "$WRAPPED_VALUE"
