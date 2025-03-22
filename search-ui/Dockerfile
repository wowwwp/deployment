FROM node:18-alpine

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./


# Install dependencies
RUN yarn
RUN yarn add @elastic/search-ui-elasticsearch-connector
RUN yarn add @babel/plugin-proposal-private-property-in-object 

COPY . .

# Build the application
RUN yarn build

EXPOSE 3000

CMD ["npm", "start"]
