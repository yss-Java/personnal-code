import matplotlib.pyplot as plt
import numpy as np

#创建数据
# x=np.linspace(0,10)
# y=np.cos(x)

#绘制折线图并设置标记样式
# plt.plot(x,y,marker='*')
# plt.plot(x,y,'o:r')
# plt.show()

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
#plt.plot(x, y, marker='o',ms = 20,mec='r')
#plt.plot(x, y, marker='o',ms = 20,mfc='r')
#plt.plot(x, y, marker='o',ms = 20,mec='r',mfc='w')
#plt.plot(x, y, marker='o',ms = 20,mec='g',mfc='g')

plt.plot(x,y,marker='o',ms=20)
plt.show()