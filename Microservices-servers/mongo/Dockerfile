FROM mongo

COPY init.json /init.json
COPY create_user.js /create_user.js
COPY import.sh /import.sh
#CMD mongoimport --host mongo --port 27017 --db jsondb --collection MyDummyCollection --type json --file /init.json --jsonArray
RUN chmod 777 /usr/local/bin/docker-entrypoint.sh \
    && ln -s /usr/local/bin/docker-entrypoint.sh /

