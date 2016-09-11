# Simple reddit bot using PRAW
# Replies to a user defined key phrase or word when it is commented
# Use as a base for other bots

import time

try:
    import praw
    print("SUCCESS: PRAW was detected on your device")
except ImportError:
    print("ERROR: PRAW is not detected on your device")
    print("The PRAW package is needed to run the bot")

user_agent = "testbot by /u/gasparek"

# create praw.reddit object
r = praw.Reddit(user_agent)

r.login()

print("Logging in...")

# Enter the keyword to search the comments for 
keywords = ['defiantly']
# cache to make sure the bot doesn't keep spamming the same comment
cache = []

# run the bot
def run():
    print("Polling comments..", end="")
    subreddit = r.get_subreddit("test")
    comments = subreddit.get_comments(limit=50)
    for comment in comments: 
        comment_text = comment.body.lower()
        match = any(string in comment_text for string in keywords)
        if comment.id not in cache and match:
            print("Match found: " + comment.id)
            comment.reply('I think you meant definitely.')
            cache.append(comment.id)
    print("Done!")

while True:
    run()
    time.sleep(10)
