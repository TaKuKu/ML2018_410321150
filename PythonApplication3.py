import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

E = Image.open("C:\Documents\Visual Studio 2017\Projects\PythonApplication3\PythonApplication3\E.png")
Eprime = Image.open("C:\Documents\Visual Studio 2017\Projects\PythonApplication3\PythonApplication3\Eprime.png")
I = Image.open("C:\Documents\Visual Studio 2017\Projects\PythonApplication3\PythonApplication3\I.png")
Key1 = Image.open("C:\Documents\Visual Studio 2017\Projects\PythonApplication3\PythonApplication3\key1.png")
Key2 = Image.open("C:\Documents\Visual Studio 2017\Projects\PythonApplication3\PythonApplication3\key2.png")
#先將需要的影像開啟
MaxIterLimit = 2
#由於運行時間相當長，最後只將執行次數設定為兩次

height = E.size[1]
width = E.size[0]
Epoch = 1
w = np.random.random(3)
#隨機生成三個w數值

while Epoch < MaxIterLimit:
    for x in range(0, height):
        for y in range(0, height):
            a = w[0] * Key1.getpixel((x, y)) + w[1] * Key2.getpixel((x, y)) + w[2] * I.getpixel((x, y))
            e = E.getpixel((x, y)) - a
            w[0] += 0.00001 * e * Key1.getpixel((x, y))
            w[1] += 0.00001 * e * Key2.getpixel((x, y))
            w[2] += 0.00001 * e * I.getpixel((x, y))
     Epoch = Epoch + 1
#按照演算法處理每筆學習資料

print(w)
output = (Eprime - (w[0] * Key1) - (w[1] * Key2)) / w[2]   
#將得出的w用於解碼加密影像上

plt.imshow(output, cmap = 'gray')

plt.show()

    
#output = np.empty((400,300))
##for x in range(0, width):
    #for y in range(0, height):
        #output.putpixel((x, y), (Eprime.getpixel((x, y)) - w[0] * Key1.getpixel((x, y)) - w[1] * Key2.getpixel((x, y)))/w[2])
#img = Image.fromarray(output)
#print(img)


E.close()
Eprime.close()
I.close()
Key1.close()
Key2.close()

