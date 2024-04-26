import reflex as rx
from sqlmodel import Field

class User(rx.Model, table=True):
    username: str
    email: str
    password: str

class Post(rx.Model, table=True):
    title: str
    content: str
    user_id: int
    author: User

class Comment(rx.Model, table=True):
    content: str
    post_id: int
    post: Post
    user_id: int
    author: User

class Like(rx.Model, table=True):
    user_id: int

class Follow(rx.Model, table=True):
    followed_username: str = Field(primary_key=True)
    follower_username: str = Field(primary_key=True)


class Notification(rx.Model, table=True):
    content: str
    user_id: int
    author: User
    read: bool