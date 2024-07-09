"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_data(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url)
        return await response.json()

