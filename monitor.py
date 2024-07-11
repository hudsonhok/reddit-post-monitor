import praw
import re
import time

def extract_keywords(title, description):
    keywords = ["3090", "4070", "4080", "4090"]     # Fill in with whatever keywords you're looking for
    def contains_keyword(text, keywords):
        return any(keyword in text for keyword in keywords)     # Might need to change to keyword.lower() for words
    if contains_keyword(title, keywords) or contains_keyword(description, keywords):
        return True
    return False

# Fill in these parameters
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent='',
)

me = reddit.user.me()
subreddit = reddit.subreddit("hardwareswap")

while True:
    new_posts = subreddit.new(limit=10)
    for post in new_posts:
        if extract_keywords(post.title, post.selftext):
            print("Newest post: ", post.title)
            print("Author: ", post.author)
            print("Description: ", post.selftext)
            print("URL: ", post.url)
            print("\n")
    time.sleep(31)