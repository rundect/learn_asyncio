import asyncio
import aiohttp
from util import async_timed, fetch_status_delay


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status_delay(session, 'https://www.example.com', 1),
                    fetch_status_delay(session, 'https://www.example.com', 1),
                    fetch_status_delay(session, 'https://www.example.com', 10)]

        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


asyncio.run(main())
