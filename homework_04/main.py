"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import init_db, async_engine, User, Post
from sqlalchemy.ext.asyncio import AsyncSession


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


async def async_main():
    await init_db()

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    await add_users_to_db(users_data),
    await add_posts_to_db(posts_data),


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
