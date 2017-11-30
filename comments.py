#!/usr/bin/python
import configparser
from imgurpython import ImgurClient
import datetime
import sys
from time import sleep
import os.path

config = configparser.ConfigParser()
config.read('/home/ubuntu/imgur_python/auth.ini')

client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')

client = ImgurClient(client_id, client_secret)


now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
if(day == 1): #need to update month and find which day NOTE:doesn't account for new year, nor leap year
    month -= 1
    if(month in [1, 3, 5, 7, 8, 10, 12]):
        day = 31
    if(month in [4, 6, 9, 11]):
        day = 30
    if(month == 2):
        day =28
else:
    day -=1
        
date = str(year) + "-" + str(month) + "-" + str(day)
date = "2017-11-20"
dateFile = "/home/ubuntu/imgur_python/galleryIds/" + date
images = open(dateFile, 'r')

users = {}

def processReply(parent, re):
    if(client.get_credits()['UserRemaining'] <= 5): #wait 
        while(client.get_credits()['UserRemaining'] <=5):
            sleep(3600)
            client.gallery_item(image)

    curReply = re
    repAuthor = curReply.author

    if(parent not in users.keys()):
        users[parent] = []

    if(repAuthor not in users.keys()):
        users[repAuthor] = []
        
    if(repAuthor not in users[parent] and repAuthor != ''):
        users[parent].append(repAuthor)

    try:
        curReplies = client.get_comment_replies(curReply.id)
    except:
        pass
    
    for r in curReplies.children[1:]:
        processReply(repAuthor, r)


for image in images:

    image = image.rstrip()
    outImageFile = "/home/ubuntu/imgur_python/commentIds/" + date + "-" + str(image)
    if(os.path.exists(outImageFile)):
        continue
                

    if(client.get_credits()['UserRemaining'] <= 5): #wait 
        while(client.get_credits()['UserRemaining'] <=5):
            sleep(3600)
            client.gallery_item(image)
    
    try:
        image = image.rstrip()
        users = {}
        item = client.gallery_item(image)
        author = item.account_url
        users[author] = []

        comments = client.gallery_comment_ids(image)
    
        for comment in comments:
            
            if(client.get_credits()['UserRemaining'] <= 5): #wait 
                while(client.get_credits()['UserRemaining'] <=5):
                    sleep(3600)
                    client.gallery_item(image)
            try:
                curComment= client.get_comment(comment)
                comAuthor = curComment.author

                if(comAuthor not in users.keys()):
                    users[comAuthor] = []
        
                if(comAuthor not in users[author] and comAuthor != ''):
                    users[author].append(comAuthor)
        
                replies = client.get_comment_replies(comment)

                for reply in replies.children[1:]:
                    processReply(comAuthor, reply)
            except:
                continue

        out = open(outImageFile, 'w')

        out.write(author)     
        for tmp in users[author]:
            out.write("," + tmp)
            out.write("\n")
        
        for user in users:
            if(user != author):
                out.write(user)
                for rep in users[user]:
                    out.write("," + rep)
                out.write("\n")

        out.close()
    except:
        continue

images.close()    

            
       
