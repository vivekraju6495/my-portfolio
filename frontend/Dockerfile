FROM node:24-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy project
COPY . .

# Build Next.js
RUN npm run build

EXPOSE 3000

# Start Next.js
CMD ["npm", "start"]
