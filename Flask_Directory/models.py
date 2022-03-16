from flask_login import UserMixin
from sqlalchemy.orm import relationship
from . import db


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = relationship('User', back_populates='posts')
    title = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    community = db.Column(db.String(250), nullable=False)
    comments = relationship('Comment', back_populates='post')


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment_author = relationship('User', back_populates='comments')
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    post = relationship('Post', back_populates='comments')


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    username = db.Column(db.String(250), nullable=False, unique=True)
    posts = relationship('Post', back_populates='author')
    comments = relationship('Comment', back_populates='comment_author')
