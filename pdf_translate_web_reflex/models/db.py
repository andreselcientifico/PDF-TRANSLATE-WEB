import reflex as rx
from datetime import datetime
from sqlmodel import Field, Column
from pgvector.sqlalchemy import Vector

class User(rx.Model, table=True):
    __tablename__ = "users"
    id: int = Field(primary_key=True)
    username : str = Field(unique=True, nullable=False, index=True)
    fullname : str = Field(nullable=False, index=True, default="Anonymous")
    email : str = Field(unique=True, nullable=False, index=True)
    password : str = Field(nullable=False)
    created_at : str = datetime.now()

    def __str__(self):
        return f"User {self.username}"
    
class Api_hug(rx.Model, table=True):
    __tablename__ = "api_hug"
    id : int = Field(primary_key=True)
    user_id : int = Field(alias='users.id')
    Api_key : str = Field()

class Post(rx.Model, table=True):
    __tablename__ = "posts"
    id: int = Field(primary_key=True)
    title: str  = Field(index=True)
    content: str = Field(index=True)
    user_id: int = Field(alias='users.id')

class embedd(rx.Model, table=True):
    __tablename__ = "embeddings"
    id : int = Field(primary_key=True)
    post_id : int = Field(alias='posts.id')
    embbedings : list[float] = Field(sa_column=Column(Vector()))

class Comment(rx.Model, table=True):
    __tablename__ = "comments"
    content: str = Field(index=True)
    post_id: int
    user_id: int

class Like(rx.Model, table=True):
    __tablename__ = "likes"
    user_id: int = Field(alias='users.id')

class Follow(rx.Model, table=True):
    __tablename__ = "follows"
    followed_username: str = Field(primary_key=True)
    follower_username: str = Field(primary_key=True)

class Notification(rx.Model, table=True):
    __tablename__ = "notifications"
    content: str = Field(index=True)
    user_id: int = Field(alias='users.id')
    read: bool = Field(default=False)