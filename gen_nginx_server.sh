#!/bin/bash

# Prompt for the domain name
read -p "Enter the domain name (e.g., api.example.com): " DOMAIN

# Define the output directory and file
OUTPUT_DIR="./ci"
CONFIG_FILE="${OUTPUT_DIR}/server.conf"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Generate the Nginx configuration
cat <<EOL > "$CONFIG_FILE"
server {
    listen 80;
    server_name $DOMAIN;

    # Redirect HTTP to HTTPS
    return 301 https://\$host\$request_uri;
}

server {
    listen 443 ssl;
    server_name $DOMAIN;

    # Specify SSL certificate and key
    ssl_certificate /etc/ssl/certs/server.crt;
    ssl_certificate_key /etc/ssl/private/server.key;

    location / {
        proxy_pass http://api-server:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host \$host;
        proxy_cache_bypass \$http_upgrade;
    }

    # Logging for debugging
    access_log /var/log/nginx/api_access.log;
    error_log /var/log/nginx/api_error.log;
}
EOL

# Confirm creation
echo "Nginx Server configuration with SSL has been written to $CONFIG_FILE"
