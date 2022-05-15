import json
import config

def load_posts():                     
    with open(config.POST_PATH, "r", encoding="utf-8") as file:
        posts = json.load(file)
    return posts

def search_post_by_content(s):
    posts =load_posts()
    result=[]
    for post in posts:
        if s.lower() in post["content"].lower():
            result.append(post)
    return result
