########################
#  pip install aiohttp
#
# 1. Asyncio фреймворк для создания событийных циклов
# 2. Пример простой асинхронной программы времён Python 3.4
# 3. Синтаксис Async / await  на замену @asyncio.coroutine и yield from
# 4. Пример асинхронного скачивания файлов
#
#########################

import asyncio
from time import time

async def print_nums():
    num = 0
    while True:
        print("num: ", num)
        num += 1
        await asyncio.sleep(1)

async def print_time():
    while True:
        count = round((time() * 1000))
        if count % 3 == 0:
            print("{} second have passed".format(count))
        await asyncio.sleep(0.1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)

if __name__=='__main__':
    print("Hello Mister!")
    asyncio.run(main())
