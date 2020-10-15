FROM node:13-slim
LABEL Joe-Ralphin <joeral333@gmail.com>
WORKDIR /app
COPY . /app
RUN apt-get update || : && apt-get install python3 -y
RUN npm i
CMD ["npm","run","start"]
EXPOSE 3000