import asyncio
from util import delay


async def hello_every_second():
    for i in range(1, 4):
        print(f"Waiting...{i} sec")
        await asyncio.sleep(1)
        print(f"Waiting {i} sec done")


async def main():
    first_delay = asyncio.create_task(delay(2))
    second_delay = asyncio.create_task(delay(3))
    print('Before hello_every_second')
    await hello_every_second()
    print('After hello_every_second')
    first_delay_result = await first_delay
    print(first_delay_result)
    second_delay_result = await second_delay
    print(second_delay_result)

asyncio.run(main())
