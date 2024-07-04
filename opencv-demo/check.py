import cv2, numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\project\images\img2.jpg', 1)
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()

# 将图像转换到 HSV (Hue-Saturation-Value) 空间，从 RGB 转换为 HSV 空间将亮度与颜色分离，以便可以轻松提取每个像素的颜色信息：
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# 定义 HSV 空间中绿色的上下阈值
lower_green = np.array([45, 100, 100])
upper_green = np.array([80, 255, 255])

# 生成掩码，仅激活落在定义的上下阈值内的像素。cv2.inRange 是一种比较操作，用于检查像素值是否在最小值和最大值之间
mask = cv2.inRange(hsv, lower_green, upper_green)

# 在原始图像和掩码之间执行 cv2.bitwise_and 操作以获取结果图像
res = cv2.bitwise_and(img, img, mask=mask)

plt.subplot(131)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original image')
plt.subplot(132)
plt.imshow(mask, cmap='gray')
plt.title('Mask on image')
plt.subplot(133)
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.title('Resulting image')
plt.show()
