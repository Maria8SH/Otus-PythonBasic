"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession


PG_CONN_URI = "postgresql+asyncpg://user:@localhost:5432/blog"

Base = declarative_base()
async_engine = create_async_engine(PG_CONN_URI, echo=False)
Session = async_sessionmaker(bind=async_engine, expire_on_commit=False, autocommit=False,)


async def get_async_session():
    async with Session() as session:
        yield session


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32), unique=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)
    posts: Mapped[list["Post"]] = relationship(back_populates="user")


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(String, nullable=False)
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=False))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="posts")


async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_users_to_db(users_data):
    async with AsyncSession(async_engine) as session:
        for user in users_data:
            new_user = User(name=user['name'], username=user['username'], email=user['email'])
            session.add(new_user)
        await session.commit()


async def add_posts_to_db(posts_data):
    async with AsyncSession(async_engine) as session:
        for post in posts_data:
            new_post = Post(user_id=post['userId'], title=post['title'], body=post['body'])
            session.add(new_post)
        await session.commit()

