import random

iterations = 1_000_000
counter = 0
for i in range(iterations):
    x = random.random()
    y = random.random()
    if (x**2 + y**2)**(1/2)<=1:
        counter += 1

print((counter/iterations)*4)