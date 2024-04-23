import asyncio


async def main():
    print('Before await')
    await asyncio.sleep(1)
    print('After await')


loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    print('Loop close')
    loop.close()
