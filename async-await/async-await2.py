import asyncio


async def main():
    task1 = asyncio.create_task(count_numbers())
    task2 = asyncio.create_task(print_phrase())

    await asyncio.gather(task1, task2)  # Собираем две задачи и запускаем их обе


async def count_numbers():
    num = 1
    while num <= 20:
        print(num)
        num += 1
        await asyncio.sleep(1)  # Даём возможность на 1 секунду отработать функции print_phrase()


async def print_phrase():
    for i in range(7):
        print("Это функция, которая работает конкурентно")
        await asyncio.sleep(3)  # Даём возможность на 3 секунды отработать функции count_numbers()

asyncio.run(main())
