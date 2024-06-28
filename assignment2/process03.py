# Multiprocessing 2 kitchens, 2 cookers, 2 dishes
# 2 process
import multiprocessing
from multiprocessing import Value
import os

from time import sleep, ctime, time

# Basket of sharing
class Basket:
    def __init__(self, eggs):
        self.eggs = Value('i', eggs)

    def use_eggs(self, index):
        with self.eggs.get_lock():
            print(f"{ctime()} Kitchen-{index} : Chef-{index} has lock with eggs remaining {self.eggs.value}")
            self.eggs.value -= 1
            print(f"{ctime()} Kitchen-{index} : Chef-{index} has released lock with eggs remaining {self.eggs.value}")

def cooking(index, basket):
    print(f"{ctime()} Kitchen-{index} : Begin cooking...PID {os.getpid()}")
    cooking_time = time()
    with basket.eggs.get_lock():
        if basket.eggs.value > 0:
            basket.eggs.value -= 1
    sleep(2)
    duration = time() - cooking_time
    print(f"{ctime()} Kitchen-{index} : Cooking done in {duration:0.2f} seconds!")

def kitchen(index, basket):
    cooking(index, basket)

if __name__ == "__main__":
    print(f'{ctime()} Main : Begin Cooking.')
    start_time = time()

    basket = Basket(50)

    # Printing main program process id
    print(f"{ctime()} Main : ID of main process: {os.getpid()}")

    # Multi processes
    kitchens = []
    for index in range(2):
        p = multiprocessing.Process(target=kitchen, args=(index, basket))
        kitchens.append(p)
        # starting process
        p.start()

    for p in kitchens:
        p.join()

    print(f"{ctime()} Main : Basket eggs remaining {basket.eggs.value}")
    duration = time() - start_time
    print(f"{ctime()} Main : Finished Cooking duration in {duration:0.2f} seconds")
