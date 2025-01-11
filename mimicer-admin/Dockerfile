# Build Stage
FROM node:22-alpine AS builder
WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm

# Copy and install dependencies using pnpm
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

# Copy application code and build
COPY . .
RUN pnpm build

# Run Stage (Using Nginx)
FROM nginx:alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy the custom NGINX configuration
COPY ./ci/nginx.conf /etc/nginx/conf.d/default.conf

# Expose the port and start NGINX
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
