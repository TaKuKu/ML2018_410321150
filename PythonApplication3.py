import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

E = Image.open("C:\Documents\Visual Studio 2017\Projects\PythonApplication3\PythonApplication3\E.png")
Eprime = Image.open("C:\Documents\Visual Studio 2017\Projects\PythonApplication3\PythonApplication3\Eprime.png")
I = Image.open("C:\Documents\Visual Studio 2017\Projects\PythonApplication3\PythonApplication3\I.png")
Key1 = Image.open("C:\Documents\Visual Studio 2017\Projects\PythonApplication3\PythonApplication3\key1.png")
Key2 = Image.open("C:\Documents\Visual Studio 2017\Projects\PythonApplication3\PythonApplication3\key2.png")
MaxIterLimit = 2

height = E.size[1]
width = E.size[0]
Epoch = 1
w = np.random.random(3)

while Epoch < MaxIterLimit:
    for x in range(0, height):
        for y in range(0, height):
            a = w[0] * Key1.getpixel((x, y)) + w[1] * Key2.getpixel((x, y)) + w[2] * I.getpixel((x, y))
            e = E.getpixel((x, y)) - a
            w[0] += 0.00001 * e * Key1.getpixel((x, y))
            w[1] += 0.00001 * e * Key2.getpixel((x, y))
            w[2] += 0.00001 * e * I.getpixel((x, y))
     Epoch = Epoch + 1


output = (Eprime - (w[0] * Key1) - (w[1] * Key2)) / w[2]   

plt.imshow(output, cmap = 'gray')

plt.show()

    
#output = np.empty((400,300))
##for x in range(0, width):
    #for y in range(0, height):
        #output.putpixel((x, y), (Eprime.getpixel((x, y)) - w[0] * Key1.getpixel((x, y)) - w[1] * Key2.getpixel((x, y)))/w[2])
#img = Image.fromarray(output)
#print(img)

#編輯中...

E.close()
Eprime.close()
I.close()
Key1.close()
Key2.close()

