import asyncio
import aiohttp
from util import fetch_status_delay


async def main():
    async with aiohttp.ClientSession() as session:
        api_a = fetch_status_delay(session, 'https://www.example.com')
        api_b = fetch_status_delay(session, 'https://www.example.com', delay=2)

        done, pending = await asyncio.wait([api_a, api_b], timeout=1)

        for task in pending:
            if task is api_b:
                print('API B too slow, cancelling')
                task.cancel()

asyncio.run(main())
