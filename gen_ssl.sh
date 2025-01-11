#!/bin/bash

# Prompt for the domain name
read -p "Enter the domain name for the SSL certificate: " DOMAIN

# Prompt for the base file name
read -p "Enter the base file name (without extension): " FILENAME

# Define the output directory
OUTPUT_DIR="./ci"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Set output file names in the ./ci folder
CERT_FILE="${OUTPUT_DIR}/${FILENAME}.crt"
KEY_FILE="${OUTPUT_DIR}/${FILENAME}.key"

# Generate a self-signed SSL certificate
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout "$KEY_FILE" -out "$CERT_FILE" \
  -subj "/CN=$DOMAIN"

# Verify creation
if [[ -f "$CERT_FILE" && -f "$KEY_FILE" ]]; then
  echo "Self-signed SSL certificate and key have been created in the ./ci folder."
  echo "Certificate: $CERT_FILE"
  echo "Key: $KEY_FILE"
else
  echo "Error: Failed to create the SSL certificate and key."
fi
