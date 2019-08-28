from app import db
from app.models import Post


def get_all():
    return Post.query.all()


def new_post(title: str, body: str) -> Post:
    post = Post(title, body)
    db.session.add(post)
    db.session.commit()
    return post
