import numpy as np
import matplotlib.pyplot as plt

# x陣列 0-9
xArray = np.arange(10); 

# y陣列=x陣列*2  0-18
yArray = xArray *  2;  

print(xArray) 
print(yArray) 

# 建立直方圖
plt.bar(xArray, yArray)

#繪圖
plt.show()

