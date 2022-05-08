from flask import Blueprint, render_template, request
import logging
from functions import *


loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")

logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="UTF-8")


@loader_blueprint.route("/post/", methods=["GET"])
def page_post_form():
    return render_template("post_form.html")


@loader_blueprint.route("/post/", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Данные не загружены")
        return "Данные не загружены"

    posts = load_json_data(POST_PATH)

    try:
        new_post = {"pic": save_picture(picture), "content": content}
    except WrongImgType:
        logging.info("Файл не картинка")
        return "Файл не картинка"
    add_post(posts, new_post)
    return render_template("post_uploaded.html", new_post=new_post)
