#!/bin/bash
alias http='docker run -it --rm mcampbell/httpie'
while true; do python updateTrigger.py; echo "esperando..."; sleep 3001; done
