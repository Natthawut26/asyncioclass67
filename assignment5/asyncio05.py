import asyncio
from random import random

# Coroutine to simulate microwave cooking
async def microwave_cooking(dish):
    # Generate a random cooking time between 1 and 2 seconds
    cooking_time = 1 + random()
    # Print the cooking time
    print(f'Microwave ({dish}): Cooking {cooking_time} seconds...')
    # Simulate the cooking time with sleep
    await asyncio.sleep(cooking_time)
    # Print the completion message
    print(f'Microwave ({dish}): Finished cooking')
    # Return the dish and cooking time
    return f' - {dish} is complete in {cooking_time} '

# Main coroutine
async def main():
    # Create tasks for cooking each dish asynchronously
    tasks = [
        asyncio.create_task(microwave_cooking('Rice')),
        asyncio.create_task(microwave_cooking('Noodle')),
        asyncio.create_task(microwave_cooking('Curry'))
    ]
    
    # Wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    # Print the number of completed tasks
    print(f"Completed tasks: {len(done)}")
    
    # Get the first completed task and print its result
    completed_task = done.pop()
    print(f"Result of completed task: {completed_task.result()}")
    
    # Print the number of pending tasks
    print(f"Pending tasks: {len(pending)}")
    
# Start the asyncio program
asyncio.run(main())

