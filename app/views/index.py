from flask import render_template, redirect, request
from flask.views import MethodView

from app import app
from app.services import posts
from app.forms import PostForm


class IndexView(MethodView):
    def get(self):
        post_qs = posts.get_all()
        form = PostForm()
        return render_template('index.html', posts=post_qs, form=form)

    def post(self):
        form = PostForm()
        if form.validate_on_submit():
            posts.new_post(request.form['title'], request.form['body'])
        return redirect('/')


app.add_url_rule('/', view_func=IndexView.as_view('posts'))
