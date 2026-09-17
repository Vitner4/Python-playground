import asyncio

async def request(name, seconds):
    print(f"{name}-запрос послан!")
    await asyncio.sleep(seconds)
    print(f"{name}-запрос получил ответ!")

    return name

async def main():
    result = await asyncio.gather(
        request("SQL", 4),
        request("API", 3),
        request("Google-search", 2),
        request("Online-status", 1)
    )

    print(result)

asyncio.run(main())