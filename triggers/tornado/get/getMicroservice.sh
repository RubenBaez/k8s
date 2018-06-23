#!/bin/bash
alias http='docker run -it --rm mcampbell/httpie'
while true; do python getTrigger.py ; echo "esperando..."; sleep 1; done
