FROM node:13-slim
LABEL Joe-Ralphin <joeral333@gmail.com>
WORKDIR /app
COPY . /app
RUN apk --no-cache add g++ gcc libgcc libstdc++ linux-headers make python
RUN npm install --quiet node-gyp -g
RUN npm i express python-shell
CMD ["npm","run","start"]
EXPOSE 3000