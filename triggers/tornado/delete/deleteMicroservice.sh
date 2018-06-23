#!/bin/bash
alias http='docker run -it --rm mcampbell/httpie'
while true; do python deleteTrigger.py; echo "esperando..."; done
