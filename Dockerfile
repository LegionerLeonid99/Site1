# Use the official Node.js image as the base image
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Set environment variables
ENV SENDGRID_API_KEY=your-sendgrid-api-key
ENV BUSINESS_EMAIL=otechhomeservices@gmail.com
ENV BUSINESS_NAME="O-TECH HOME SERVICES LTD"
ENV BUSINESS_PHONE=02030261006
ENV FRONTEND_URL=http://localhost:5173
ENV ALLOWED_ORIGINS="http://localhost:5173,http://127.0.0.1:5173"
ENV API_RATE_LIMIT=100
ENV VITE_API_BASE_URL=/api

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Copy the .env file for environment variables (if present)
COPY .env* ./

# Build the Vue application
RUN npm run build

# Expose the port the app runs on
EXPOSE 3001

# Command to run the application
CMD ["npm", "run", "server"]