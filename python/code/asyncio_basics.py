import asyncio


async def task(name, seconds):
    print(f"{name} начал!")

    await asyncio.sleep(seconds)

    print(f"{name} закончил!")

    return name


async def test_one():
    print(await task("A", 3))
    print(await task("B", 2))
    print(await task("C", 1))


async def main():
    results = await asyncio.gather(
        task("A", 3),
        task("B", 2),
        task("C", 1)
    )

    print(results)


asyncio.run(test_one())
        