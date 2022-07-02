import asyncio
import random
import time
import datetime as dt


# Пример работы асинхронных функций

# 1 функция - compliments()
# Запускается, а затем ждёт, когда закончат свою работу функции say_hello_to_you() и say_compliment(),
# после чего завершается. Все эти функции (compliments(), say_hello_to_you() и say_compliment()) являются
# корутинами. Так называют функции, объявленные ключевым словом "async":
async def compliments():
    start_time = dt.datetime.now()
    print(f"Функция \"compliments\" запущена в {start_time.strftime('%X')}")

    await say_hello_to_you("Настенька")
    await say_compliment()

    end_time = dt.datetime.now()
    print(f"Функция \"compliments\" завершена в {end_time.strftime('%X')}")
    time_diff = end_time - start_time
    print(f"Время работы функции: {time_diff.total_seconds()} секунд(ы)")


async def say_hello_to_you(name):
    print(f"Привет, {name}!")
    await asyncio.sleep(1)


async def say_compliment():
    compliments_list = [
        "Ты сегодня хорошо выглядишь (* ^ ω ^)",
        "Потрясный прикид!",
        "Твой загадочный взгляд сразил меня наповал..."
    ]
    random_compliment = random.choice(compliments_list)
    print(random_compliment)
    await asyncio.sleep(2)


# 2 функция - compliments2()
# Точно так же запускается, но теперь корутины say_hello_to_you2() и say_compliment2() являются тасками.
# Корутины, которые объявили тасками, выполняют свою работу конкурентно, т.е. в случае, если один таск (корутина)
# на какое-то время приостанавливает свою работу (спит), то включается второй таск, и таким образом в работе корутин
# не возникает простоев - функции всегда выполняют какую-то работу и не филонят
async def compliments2():
    start_time = dt.datetime.now()
    print(f"Функция \"compliments2\" запущена в {start_time.strftime('%X')}")

    task1 = asyncio.create_task(say_hello_to_you2("Артемий"))
    task2 = asyncio.create_task(say_compliment2())
    await asyncio.gather(task1, task2)

    end_time = dt.datetime.now()
    print(f"Функция \"compliments2\" завершена в {end_time.strftime('%X')}")
    time_diff = end_time - start_time
    print(f"Время работы функции: {time_diff.total_seconds()} секунд(ы)")


async def say_hello_to_you2(name):
    print(f"Привет, {name}!")
    await asyncio.sleep(1)


async def say_compliment2():
    compliments_list = [
        "Ты сегодня хорошо выглядишь (* ^ ω ^)",
        "Потрясный прикид!",
        "Твой загадочный взгляд сразил меня наповал..."
    ]
    random_compliment = random.choice(compliments_list)
    print(random_compliment)
    await asyncio.sleep(2)


# Запуск
asyncio.run(compliments())

print("=================================\n=================================")

asyncio.run(compliments2())
