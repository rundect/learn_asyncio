import asyncio


async def add_one(number: int) -> int:
    return number + 1


async def main() -> None:
    print('Before awaiting')
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print('After first awaiting')
    two_plus_one = await add_one(2)
    print(two_plus_one)


asyncio.run(main())
