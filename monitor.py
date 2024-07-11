import praw
import time
import tkinter as tk
from tkinter import ttk
import threading
import winsound
import webbrowser

# Play Sound
def function_sound():
    winsound.PlaySound('bell.wav', winsound.SND_ASYNC)

# Extract keywords
def extract_keywords(title, description):
    keywords = ["3090", "4070", "4080", "4090"]  # Fill in with whatever keywords you're looking for
    def contains_keyword(text, keywords):
        return any(keyword in text for keyword in keywords)
    if contains_keyword(title, keywords) or contains_keyword(description, keywords):
        return True
    return False

# Set up Reddit API
# User agent you can name whatever but general convention is "<Name of Script/Bot> by u/<Reddit Username>"
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent=''
)

# Fetch new posts
def fetch_new_posts():
    subreddit = reddit.subreddit("hardwareswap")
    while True:
        new_posts = subreddit.new(limit=3)
        for post in new_posts:
            if extract_keywords(post.title, post.selftext) and post.title not in [info[0] for info in post_info]:
                post_info.append((post.title, post.author.name, post.selftext, post.url))
                function_sound()
                update_gui()
        time.sleep(31)

## **Tkinter GUI** ##
# Update the GUI with new posts
def update_gui():
    # Clear existing widgets within frame
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Add new widgets for each post
    for i, post in enumerate(reversed(post_info)):
        # Title widget
        title = tk.Label(frame, text=post[0], wraplength=500)
        title.grid(row=i*2, column=0, columnspan=3, sticky='ew')
        
        # View link widget
        view_link = tk.Label(frame, text="View", fg="blue", cursor="hand2", wraplength=500)
        view_link.grid(row=i*2, column=3, sticky='ew')
        view_link.bind("<Button-1>", lambda e, url=post[3]: open_url(url))
        
        # Remove button widget
        remove_button = tk.Button(frame, text="Remove", command=lambda p=post: remove_post(p))
        remove_button.grid(row=i*2, column=4, sticky='ew')
        
        separator = ttk.Separator(frame, orient='horizontal')
        separator.grid(row=i*2 + 1, column=0, columnspan=5, sticky='ew', pady=5)

    # Configure columns to expand
    for col in range(5):
        frame.grid_columnconfigure(col, weight=1)

# Remove a specific post
def remove_post(post):
    post_info.remove(post)
    update_gui()

# Clear all posts
def clear_all_posts():
    post_info.clear()
    update_gui()

# Open URL in a browser
def open_url(url):
    webbrowser.open(url)

# Initialize Tkinter GUI
root = tk.Tk()
root.title("Reddit Post Monitor")
root.geometry("800x600")

frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

clear_button = tk.Button(root, text="Clear All", command=clear_all_posts)
clear_button.pack()

# Fetching posts in a separate thread
# Contains posts in tuple format (title, author name, description, url)
post_info = []
threading.Thread(target=fetch_new_posts, daemon=True).start()

root.mainloop()
