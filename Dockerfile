FROM node:13-slim
WORKDIR /app
COPY . /app
RUN apt-get install python3.6
RUN npm i express python-shell
CMD ["npm","run","start"]
EXPOSE 3000