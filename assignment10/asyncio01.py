from random import random
import asyncio
import time

# Coroutine to generate work
async def producer(queue):
    start_time = time.time()  # Start time for producer
    print('Producer: Running')
    # Generate work
    for i in range(10):
        # Generate a value
        value = i
        # Block to simulate work
        await asyncio.sleep(random())
        # Add to the queue
        print(f'> Producer put {value}')
        await queue.put(value)
    # Send an all done signal
    await queue.put(None)
    print('Producer: Done')
    end_time = time.time()  # End time for producer
    print(f'Producer execution time: {end_time - start_time:.2f} seconds')

# Coroutine to consume work
async def consumer(queue):
    start_time = time.time()  # Start time for consumer
    print('Consumer: Running')
    # Consume work
    while True:
        # Get a unit of work
        item = await queue.get()
        # Check for stop signal
        if item is None:
            break
        # Report
        print(f'\tConsumer got {item}')
    print('Consumer: Done')
    end_time = time.time()  # End time for consumer
    print(f'Consumer execution time: {end_time - start_time:.2f} seconds')

# Entry point coroutine
async def main():
    # Create the shared queue
    queue = asyncio.Queue()
    # Run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# Start the asyncio program
asyncio.run(main())
