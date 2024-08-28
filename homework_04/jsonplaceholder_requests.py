"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
import asyncio


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url)
        return await response.json()


async def fetch_users_data():
    return await fetch_json(url=USERS_DATA_URL)


async def fetch_posts_data():
    return await fetch_json(url=POSTS_DATA_URL)
