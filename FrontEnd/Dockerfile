# frontend/Dockerfile
FROM node:18-slim

# Set working directory
WORKDIR /PitStopNews/Frontend

# Install dependencies
COPY package*.json /PitStopNews/Frontend
COPY public/ /PitStopNews/Frontend/public
COPY src/ /PitStopNews/Frontend/src

COPY vite.config.ts /PitStopNews/Frontend
COPY tsconfig.json /PitStopNews/Frontend
COPY env.d.ts /PitStopNews/Frontend
COPY index.html /PitStopNews/Frontend

RUN npm install


# Build the Vue.js application
# RUN npm run build

# Expose the port the app runs on
EXPOSE 8080

# Command to serve the app
CMD ["npm", "run", "dev"]
