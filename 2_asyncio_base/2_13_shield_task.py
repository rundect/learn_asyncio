import asyncio
from util import delay


async def main():
    delay_task = asyncio.create_task(delay(2))
    timeout = 1
    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), timeout)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print(f"Задача заняла более {timeout} с, скоро она закончится!")
        result = await delay_task
        print(result)


asyncio.run(main())
