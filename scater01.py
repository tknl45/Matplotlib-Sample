import numpy as np
import matplotlib.pyplot as plt

# x陣列 0-9
xArray = np.arange(10); 

# y陣列=x陣列*2  0-18
yArray = xArray *  2;  

# 每個點的大小圈圈設定
area = np.pi * 10 * yArray

# 每個點顏色設定
colors = np.random.rand(10)

# 建立分散圖
plt.scatter(xArray, yArray, s=area, c=colors, alpha=0.5)

#繪圖
plt.show()