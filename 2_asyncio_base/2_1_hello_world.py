import asyncio


async def my_coroutine() -> None:
    print('Hello world!')

asyncio.run(my_coroutine())
