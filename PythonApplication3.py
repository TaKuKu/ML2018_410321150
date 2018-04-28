import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

E = Image.open("E.png")
Eprime = Image.open("Eprime.png")
I = Image.open("I.png")
Key1 = Image.open("key1.png")
Key2 = Image.open("key2.png")
MaxIterLimit = 100

height = E.size[1]
width = E.size[0]
Epoch = 1
w = np.random.random((1,3))

while Epoch < MaxIterLimit or < 0.01:
    for y in height:
        for x in width:




E.close()
Eprime.close()
I.close()
Key1.close()
Key2.close()

