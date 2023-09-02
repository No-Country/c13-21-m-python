ARG NODE_VERSION=18.16.1
FROM node:${NODE_VERSION} as base

WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev

COPY . .
RUN npm run build

EXPOSE 3000
#CMD [ "npm", "run", "start" ]
CMD [ "npm", "start" ]


#FROM nginx:alpine
#ADD ./config/nginx.conf /etc/nginx/nginx.d/default.conf
#COPY --from=base /app/dist /var/www/app
#EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]
