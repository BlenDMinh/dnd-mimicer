# Build Stage
FROM node:22-alpine AS builder
WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm

# Copy and install dependencies using pnpm
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

ARG VITE_API_HOST
ARG VITE_API_KEY
RUN echo "VITE_API_HOST=$VITE_API_HOST" > .env && \
    echo "VITE_API_KEY=$VITE_API_KEY" >> .env

# Copy application code and build
COPY . .
RUN pnpm build

# Run Stage (Using Nginx)
FROM nginx:alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose the port and start NGINX
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
