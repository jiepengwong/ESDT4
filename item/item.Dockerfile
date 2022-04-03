FROM node:14.16.0
WORKDIR /usr/src/app
COPY package*.json /usr/src/app/
RUN npm install
COPY ./item.js ./
CMD [ "nodemon", "./item.js" ]

