# a
def iter_01():
    while True:
        yield 0
        yield 1
it = iter_01()
for _ in range(6):
    print(next(it))
# b
import random

def iter_random():
    while True:
        yield random.choice([0, 1])
it = iter_random()
for _ in range(6):
    print(next(it))
# c
def iter_cycle():
    while True:
        yield 0
        yield 1
        yield 0
        yield -1
it = iter_cycle()
for _ in range(6):
    print(next(it))