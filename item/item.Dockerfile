FROM node:16
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 5001
CMD [ "node", "item.js" ]



# FROM node:14.16.0
# WORKDIR /usr/src/app
# COPY package*.json /usr/src/app/
# RUN npm install
# COPY . /usr/src/app
# CMD [ "node", "./item.js" ]

