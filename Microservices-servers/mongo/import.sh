#!/bin/bash
importando..
mongoimport --host localhost --port 27017  --db jsondb --collection coll --type json --file /init.json --jsonArray
echo "############################"
echo "##### Datos importados #####"
echo "############################
