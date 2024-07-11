# Reddit Scraper Script
## Overview
This script scrapes the newest post from the r/hardwareswap subreddit based on a specified keyword and outputs the details of the post. This can work with any subreddit and it is built using Python Reddit API Wrapper (PRAW). I saw this as a nice opportunity to learn about interacting with Reddit's API through PRAW and automating tasks with Python. 

## Features
* Scrapes the newest post from r/hardwareswap subreddit for a specified keyword.
* Outputs the title, author, and URL of the post.
* Easy to customize for different keywords and subreddits.

## Prerequisites
Before running the script, ensure you have the following:
* Windows OS
* Python 3.6 or higher installed on your machine
* PRAW library installed. You can install it via pip:
`pip install praw`

## Setup

1. Reddit API Credentials
    * Create a Reddit account if you don't have one.
    * Go to Reddit's app preferences and create a new application.
    * Select "script" as the application type.
    * Click "create app".
    * Note the 'client_id' and 'client_secret' values.

2. Clone the repository
`git clone https://github.com/hudsonhok/reddit_post_monitor.git`

3. Change subreddit and/or keywords
    * Customize the keywords you're looking for within the subreddit of your choice.

4. Input Reddit credentials
    * Fill in the `reddit` parameters including `client_id`, `client_secret`, and `user_agent`.

5. Execute file
    * Run `python monitor.py`
