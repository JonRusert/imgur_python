#!/usr/bin/python
import configparser
from imgurpython import ImgurClient
import datetime

config = configparser.ConfigParser()
config.read('/home/ubuntu/imgur_python/auth.ini')

client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')

client = ImgurClient(client_id, client_secret)

now = datetime.datetime.now()
date = str(now.year)
date = date + "-" + str(now.month)
date = date + "-" + str(now.day)
dateFile = "/home/ubuntu/imgur_python/galleryIds/" + date
out = open(dateFile, 'w')

#extracts the items (images) on the front page of imgur.
items = client.gallery()

i=0
for item in items:
    if i >= 50:
        break
    else:
        i+=1
    out.write(item.id)
    out.write('\n')

out.close()
