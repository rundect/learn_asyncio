import asyncio
from util import delay


async def main():
    delay_task = asyncio.create_task(delay(2))
    timeout = 1
    try:
        result = await asyncio.wait_for(delay_task, timeout=timeout)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? {delay_task.cancelled()}')


asyncio.run(main())
