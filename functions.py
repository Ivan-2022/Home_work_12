import json
from json import JSONDecodeError
from config import POST_PATH, UPLOAD_FOLDER
from exceptions import DataJsonError, WrongImgType


def load_json_data(path):
    try:
        with open(path, 'r', encoding="UTF-8") as file:
            return json.load(file)

    except (FileNotFoundError, JSONDecodeError):
        raise DataJsonError


def search_posts_by_substring(posts, substring):
    posts_found = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_found.append(post)
    return posts_found


def save_picture(picture):
    allowed_type = ["jpg", "png", "gif", "jpeg"]
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in allowed_type:
        raise WrongImgType(f"Загруженный файл - не картинка. Можно только {', '.join(allowed_type)}")
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    return picture_path


def add_post(post_list, post):
    post_list.append(post)
    with open(POST_PATH, "w", encoding="UTF-8") as file:
        json.dump(post_list, file, ensure_ascii=False)
