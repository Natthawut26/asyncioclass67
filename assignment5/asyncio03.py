# example of waiting for the first task to fail
from random import random
import asyncio

# Coroutine to execute in a new task
async def task_coro(arg):
    # Generate a random value between 0 and 1
    value = random()
    # Block for a moment
    await asyncio.sleep(value)
    # Report the value
    print(f'> Task {arg} done with {value}')
    # Conditionally fail
    if value < 0.5:
        raise Exception(f'Something bad happened in task {arg}')

# Main coroutine 
async def main():
    # Create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # Wait for the first task to complete 
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # Report results
    print('Done')
    # Get the first task to complete
    first = done.pop()
    print(first)

# Start the asyncio program
asyncio.run(main())
