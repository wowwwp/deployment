# Use an official Node.js runtime as the base image
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json ./
COPY package-lock.json ./


# Install dependencies
RUN yarn
RUN yarn add @elastic/search-ui-elasticsearch-connector
RUN yarn add @babel/plugin-proposal-private-property-in-object 
# Copy the rest of the application code
COPY . .

# Build the application
RUN yarn build
# RUN npm run build

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]
