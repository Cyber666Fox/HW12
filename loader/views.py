from fileinput import filename
import logging
import loader.utils
import main.utils
from flask import Blueprint, render_template,request
from config import UPLOAD_FOLDER

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder= "templates")

@loader_blueprint.route("/post", methods=["GET"])
def post_form_page():
    return render_template("post_form.html")

@loader_blueprint.route("/post", methods=["POST"])
def post_process():
    logging.info ("Обработка поста")
    picture = request.files.get("picture")
    if not loader.utils.file_check(picture):
        logging.info("Файл не является картинкой")
        return "Файл не является картинкой"
    content = request.form.get("content")
    if not picture or not content:
        logging.info ("Данные не загружены, отсутствует чать данных")
        return "Не все поля заполнены" 

    posts = main.utils.load_posts()
    picture_path=(f"{UPLOAD_FOLDER}/{picture.filename}")
    picture.save(picture_path)
    new_post = {"pic":picture_path, "content":content}
    posts.append(new_post)
    loader.utils.dump_posts(posts)

    return render_template("post_uploaded.html", new_post=new_post)
