# Asynchronous breakfast
import asyncio
from time import sleep, time

async def make_coffee():
    print("Start making coffee")
    await asyncio.sleep(1)  # Initial step taking 1 second
    print("Pouring coffee")
    await asyncio.sleep(5)  # Additional step taking 5 seconds
    print("Coffee is ready!")

async def fry_eggs():
    print("Start frying eggs")
    await asyncio.sleep(1)  # Initial step taking 1 second
    print("Cooking eggs")
    await asyncio.sleep(3)  # Additional step taking 3 seconds
    print("Eggs are ready!")

async def main():
    await asyncio.gather(make_coffee(), fry_eggs())

# Run the main function
asyncio.run(main())
