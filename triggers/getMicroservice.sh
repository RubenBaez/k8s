#!/bin/bash
alias http='docker run -it --rm mcampbell/httpie'
while true; do http http://192.168.99.100:32218/; echo "esperando..."; sleep 1; done
