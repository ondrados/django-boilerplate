#!/bin/sh

# Takes all env variables with prefix "DJANGO_" and write them in .env without prefix
export | grep DJANGO_ | sed -e 's/DJANGO_//g' | sed -e 's/declare -x //g' > .env
