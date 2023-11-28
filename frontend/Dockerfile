FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY . /app
RUN npm config set registry https://registry.npm.taobao.org
RUN npm install

CMD ["npm", "run", "dev"]
