#!/bin/bash

# Prompt for the domain name
read -p "Enter the domain name (e.g., example.com): " DOMAIN

# Define the output directory and file
OUTPUT_DIR="./ci"
CONFIG_FILE="${OUTPUT_DIR}/client.conf"

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
    ssl_certificate /etc/ssl/certs/client.crt;
    ssl_certificate_key /etc/ssl/private/client.key;

    root /usr/share/nginx/html;

    location / {
        try_files \$uri \$uri/ /index.html;
    }

    # Serve static files (e.g., JS, CSS)
    location /static/ {
        expires 30d;
        add_header Cache-Control "public, no-transform";
    }

    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
    }

    # Logging for debugging
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
}
EOL

# Confirm creation
echo "Nginx Client configuration with SSL has been written to $CONFIG_FILE"
