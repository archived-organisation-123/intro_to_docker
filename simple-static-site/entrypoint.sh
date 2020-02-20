#!/bin/bash
echo "Static site is being served http://0.0.0.0:8080..."
exec nginx -g "daemon off;"
