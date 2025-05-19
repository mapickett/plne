import asyncio
import time

# SYNCHRONOUS
def sync_f():
    print('one ', end='')
    time.sleep(1)
    print('two ', end='')


# ASYNCHRONOUS
async def async_f():
    print('one ', end='')
    await asyncio.sleep(1)
    print('two ', end='')

# async def f():
#     pass
#
# async def g():
#     await f()   # pause here and come back to g() when f() is ready

async def main():   # top level coroutine
    # tasks = [async_f(), async_f(), async_f()]
    tasks = [async_f() for _ in range(3)]   # same thing using list comprehension

    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())     # creates the event loop
end = time.time()
print(f'Execution time(ASYNC): {end - start:.0f}')

print('\n')
start = time.time()
for _ in range(3):
    sync_f()
end = time.time()
print(f'Execution time(SYNC): {end - start:.0f}')