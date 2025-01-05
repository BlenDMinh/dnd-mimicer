FROM node:22-alpine AS builder
WORKDIR /app
COPY package.json yarn.lock* ./
RUN yarn install --frozen-lockfile
COPY . .
RUN yarn vite build

# Run Stage (Using Nginx)
FROM nginx:alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist /var/www/html

# Copy the custom NGINX configuration
COPY nginx.conf /etc/nginx/conf.d/nginx.conf

# Expose the port and start NGINX
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]