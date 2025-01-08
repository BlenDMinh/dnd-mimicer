# Use an official Node.js runtime as a parent image
FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

RUN ls -la /app

# Build the application
RUN npm run build

# Expose the port the app runs on
EXPOSE 8080

# Command to run the Vite development server
CMD ["npm", "run", "dev"]