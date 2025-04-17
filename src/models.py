from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
db = SQLAlchemy()
class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    # is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name" : self.first_name,
            "last_name" : self.last_name
            # do not serialize the password, its a security breach
        }
class Media(db.Model):
    __tablename__ = "medias"
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    post: Mapped['Post'] = relationship('Post', back_populates = 'media')
    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id,
        }
class Post(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    media: Mapped[list['Media']] = relationship('Media', back_populates = 'post')
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
        }
class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id,
        }
class Follower(db.Model):
    __tablename__ = "followers"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user_to: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "user_from": self.user_from,
            "user_to": self.user_to,
        }