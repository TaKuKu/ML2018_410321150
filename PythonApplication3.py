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

while Epoch < MaxIterLimit:
    for y in height:
        for x in width:
            a = w[0] * Key1.getpixel((x, y)) + w[1] * Key2.getpixel((x, y)) + w[2] * I.getpixel((x, y))
            e = E.getpixel((x, y)) - a
            w[0] += 0.00001 * e * Key1[x][y]
            w[1] += 0.00001 * e * Key2[x][y]
            w[2] += 0.00001 * e * I[x][y]
    Epoch += 1


#編輯中...

E.close()
Eprime.close()
I.close()
Key1.close()
Key2.close()

