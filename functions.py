import json
POST_PATH = "posts.json"


def load_posts(POST_PATH):
    with open(POST_PATH, 'r', encoding='utf-8') as f:
        file = json.load(f)
    return file




def search_post(word_search):
    data = load_posts(POST_PATH)
    con = []
    for post in data:
        if word_search.lower() in post['content'].lower():
            con.append(post)
    return con


def save_picture_page(picture):
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path

def add_post_in_posts(post):
    posts = load_posts(POST_PATH)
    posts.append(post)
    with open(POST_PATH, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=4, sort_keys=True)
    return post
