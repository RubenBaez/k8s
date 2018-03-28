#!/bin/bash
mongoimport --host localhost --port 27017  --db jsondb --collection coll --type json --file /init.json --jsonArray
echo "##### Datos importados #####"
