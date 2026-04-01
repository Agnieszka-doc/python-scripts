import random
def random_walk(start):
    x = start
    while True:
        yield x # zwraca aktualną pozyjcę
        step = random.choice([-1, 1]) # losuje krok
        x += step # przesunięcie

walker = random_walk(0)
for _ in range(100):
    position = next(walker)
print("Final position:", position)

for i in range(5):
    walker = random_walk(0)
    
    for _ in range(100):
        position = next(walker)
    print(f"Experiment {i+1}: {position}")
	