import json
import config

def dump_posts (posts):
   with open (config.POST_PATH, "w", encoding="utf-8") as file:
      json.dump(posts, file,ensure_ascii=False)

def file_check (file):
   ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
   filename = file.filename
   extension = filename.split(".")[-1]
   if extension in ALLOWED_EXTENSIONS:
      return True
   else:
   	return False
