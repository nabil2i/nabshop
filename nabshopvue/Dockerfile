FROM node:18.15.0-alpine
RUN addgroup -S app && adduser -S -G app app
USER app

WORKDIR /app
COPY --chown=app:node package*.json ./
RUN npm install
COPY --chown=app:node . .

EXPOSE 8080 

CMD ["npm", "run", "serve"]
