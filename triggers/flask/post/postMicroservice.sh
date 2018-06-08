#!/bin/bash
alias http='docker run -it --rm mcampbell/httpie'
while true; do python postTrigger.py; echo "esperando..."; sleep 1; done
