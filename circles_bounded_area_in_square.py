import numpy as np
import random as ra

def f(x, y):
    r1 = np.sqrt(x**2 + (y-4)**2)
    return r1

def g(x, y):
    r2 = np.sqrt((x-4)**2 + y**2)
    return r2

def getProbability(n):
    counter = 0
    darkYellow = 0
    squareArea = 4*4

    while n > counter:
        x = ra.uniform(0, 4)
        y = ra.uniform(0, 4)

        if (f(x, y) <= 4 and g(x, y) <= 4):
            darkYellow += 1
        counter += 1
    
    probabilityDarkYellow = (darkYellow / n)
    circlesArea = squareArea * probabilityDarkYellow
    probabilityDarkYellow_percentage = round((darkYellow / n)*100,2)

    print(f'Estimated area is: {circlesArea} cm2. Out of {n} times, {darkYellow} coordinates were inside the dark yellow area.')
    
getProbability(10000)
