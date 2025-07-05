# Use official Node.js image as the base
FROM node:18.12.1-bullseye-slim

# Update npm to a specific version
RUN npm install -g npm@9.1.3

# Add application files
ADD package.json .
ADD server.js .
ADD utils/dealers.json /utils/dealers.json

# Install dependencies
RUN npm install

# Document the port the app listens on
EXPOSE 80

# Set default port environment variable
ENV PORT=80

# Start the Node.js app
CMD [ "npm", "start" ]
