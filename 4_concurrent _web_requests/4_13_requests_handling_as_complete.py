import asyncio
import aiohttp
from util import async_timed, fetch_status_delay


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        fetchers = [asyncio.create_task(fetch_status_delay(session, url)),
                    asyncio.create_task(fetch_status_delay(session, url)),
                    asyncio.create_task(fetch_status_delay(session, url))]

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')

        for done_task in done:
            print(await done_task)


asyncio.run(main())
