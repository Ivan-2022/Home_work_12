from flask import Blueprint, render_template, request
import logging
from functions import load_json_data, search_posts_by_substring
from config import POST_PATH
from exceptions import DataJsonError

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="UTF-8")


@main_blueprint.route("/")
def page_index():
    logging.info("открытие главной страницы")
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    s = request.args.get("s", "")
    logging.info("Выполняется поиск")
    try:
        posts = load_json_data(POST_PATH)
    except DataJsonError:
        return "Проблема с открытием файла постов"

    filtered_posts = search_posts_by_substring(posts, s)
    return render_template("post_list.html", posts=filtered_posts, s=s)
