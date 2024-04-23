import asyncio


async def hello_world_message() -> str:
    print('Before sleep')
    await asyncio.sleep(1)
    print('After sleep')
    return 'Hello World!'


async def main() -> None:
    print('Before await')
    message = await hello_world_message()
    print('After await')
    print(message)


asyncio.run(main())
