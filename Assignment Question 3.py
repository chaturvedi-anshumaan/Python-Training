import numpy as np
import collections
from numpy import random
x = random.randint(0,9,200)
print('Array:\n ',x)
value, counts = np.unique(x, return_counts=True)
print('Using numpy method, Element counter \n', dict(zip(value, counts)))
print("==================================================================================================")
print("============Using non numpy method================================================================\n")
counter = collections.Counter(x)
print('Counter using non numpy method \n',counter)
