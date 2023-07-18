#!/bin/sh

CMD_LINE="node_modules/http-server/bin/http-server"
CMD_PORT="8001"
CMD_PWD=" ./"

if [[ $# -eq 0 ]]; then
  CMD_SECURE=""
else
  if [[ $1 = "secure" ]]; then
    CMD_SECURE="-S --cert cert.pem --key key.pem"
    echo "enabling SSL/TLS"
  fi
fi

${CMD_LINE} ${CMD_SECURE} -p ${CMD_PORT} ${CMD_PWD} 
