import asyncio
from util import delay


async def main():
    sleep_for_three = asyncio.create_task(delay(2))
    print(sleep_for_three)
    sleep_again = asyncio.create_task(delay(1))
    print(sleep_again)
    sleep_once_more = asyncio.create_task(delay(3))
    print(sleep_once_more)
    sleep_for_three_result = await sleep_for_three
    print(sleep_for_three_result)
    sleep_again_result = await sleep_again
    print(sleep_again_result)
    sleep_once_more_result = await sleep_once_more
    print(sleep_once_more_result)


asyncio.run(main())
