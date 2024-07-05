# Concurrently breakfast
import asyncio
from time import sleep, time

async def make_coffee():  # Task 1
    print("coffee: prepare ingredients")
    sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5)  # 2: pause, another tasks can be run
    print("coffee: ready")

async def fry_eggs():  # Task 1
    print("eggs: prepare ingredients")
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3)  # 2: pause, another tasks can be run
    print("eggs: ready")

async def main():  # Task 1
    start = time()
    await asyncio.gather(
        make_coffee(),
        fry_eggs()
    )
    print(f"breakfast is ready in {time()-start} min")

# Run the main function
asyncio.run(main())
