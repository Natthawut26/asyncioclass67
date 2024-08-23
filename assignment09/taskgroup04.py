# example of asyncio task group with a canceled task
import asyncio

# coroutine task
async def task1():
    # Sleep to simulate waiting
    await asyncio.sleep(1)
    # Report a message
    print('Hello from coroutine 1')

# coroutine task
async def task2():
    # Sleep to simulate waiting
    await asyncio.sleep(1)
    # Report a message
    print('Hello from coroutine 2')

# coroutine task
async def task3():
    # Sleep to simulate waiting
    await asyncio.sleep(1)
    # Report a message
    print('Hello from coroutine 3')

# asyncio entry point
async def main():
    # Create task group
    async with asyncio.TaskGroup() as group:
        # Run first task
        t1 = group.create_task(task1())
        # Run second task
        t2 = group.create_task(task2())
        # Run third task
        t3 = group.create_task(task3())
        # Wait a moment
        await asyncio.sleep(0.5)
        # Cancel the second task
        t2.cancel()
    # Check the status of each task
    print(f'Task1: done={t1.done()}, cancelled={t1.cancelled()}')
    print(f'Task2: done={t2.done()}, cancelled={t2.cancelled()}')
    print(f'Task3: done={t3.done()}, cancelled={t3.cancelled()}')

# Entry point
asyncio.run(main())
