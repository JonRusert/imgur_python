import configparser
from imgurpython import ImgurClient
import datetime
import sys

config = configparser.ConfigParser()
config.read('/home/ubuntu/imgur_python/auth.ini')

client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')

client = ImgurClient(client_id, client_secret)

print(client.get_credits())
