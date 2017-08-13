#!/usr/bin/python

"""Pybot: a bot for reddit"""

import praw
import pdb
import re
import os

reddit = praw.Reddit('Pybot')
# here's the subreddit it's monitoring
subreddit = reddit.subreddit('pythonforengineers')

# text file used as a database for already replied to posts
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

    if submission.id not in posts_replied_to:
        # phrase or word to monitor for
        if re.search("python", submission.title, re.IGNORECASE) or re.search("test", submission.title, re.IGNORECASE):
            submission.reply("I'm a real boy!")

            print("!!! Pybot replying to : ", submission.title)

            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
