from flask import Blueprint, render_template,request
import main.utils
import logging

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

@main_blueprint.route("/")
def main_page():
    return render_template("index.html")

@main_blueprint.route("/search")
def post_list_page():
    logging.info ("Обработка поискового запроса")
    s = request.args.get("s", "")
    try:
        posts=main.utils.search_post_by_content(s) 
    except:
        logging.error("Проблема с открытием файла")
        return "Проблема с открытием файла"
    return render_template("post_list.html", posts=posts, search=s)
