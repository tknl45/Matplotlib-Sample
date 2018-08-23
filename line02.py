# 圖表加上 x 座標以及x, y的label
# 引用
import matplotlib.pyplot as plt
import numpy as np

# 畫出座標 (0,0) (1,1) (2,4) (3,9) 連成的線
xArray = np.arange(4); 
print(xArray) # [0,1,2,3]


# 設定 X座標，Y座標，畫實線
plt.plot(xArray,xArray*0, '-')
plt.ylabel('數字')

# 加入設定 X座標，Y座標。圓點(o)
plt.plot(xArray, xArray*1 ,'o')
plt.ylabel('數字')



# 加入設定 X座標，Y座標。線換成紅色的點r代表red，小圓點(.)
plt.plot(xArray, xArray*2 ,'r.--')
plt.ylabel('數字')

#b代表藍色、s代表方塊，g代表綠色，^代表三角形
# 加入設定 X座標，Y座標。線換成紅色的點r代表red，o代表圓點 虛線(-.)
plt.plot(xArray, xArray*3 ,'>-.')
plt.ylabel('數字')

#藍色方塊座標點，圓點虛線(:)串接
plt.plot(xArray, xArray*4 ,'bs:')
plt.ylabel('數字')

#pixel
plt.plot(xArray, xArray*-2 ,',')
plt.ylabel('數字')

#三角形座標點
plt.plot(xArray, xArray*-3 ,'^')
plt.ylabel('數字')

#倒三角形座標點
plt.plot(xArray, xArray*-4 ,'gv')
plt.ylabel('數字')


# 繪圖
plt.show()