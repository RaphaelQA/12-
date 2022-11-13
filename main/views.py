import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import search_post

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


@main_blueprint.route('/search/')
def search():
    search_query = request.args.get("s", "")
    logging.info('Выполняю поиск')
    try:
        posts = search_post(search_query)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return "Файл не найден :("
    except JSONDecodeError:
        return "Невалидный файл"
    return render_template("post_list.html", query=search_query, posts=posts)