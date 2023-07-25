#!/bin/bash

server=''

source /var/www/$server/.venv/bin/activate
python3 /var/www/$server/src/bot.py >> /var/www/$server/logs/out.log &>> /var/www/$server/logs/error.log
deactivate
