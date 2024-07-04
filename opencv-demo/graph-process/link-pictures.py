from PIL import Image

img1 = Image.open("D:\project\images\img2.jpg")
img2 = Image.open("D:\project\images\img1.jpg")

# 水平合并两张图片
# 构建一张图片, 宽度是两张图片宽度之和, 高度为两张图片高度较大者
img = Image.new("RGB", size=(img1.width + img2.width, max(img1.height, img2.height)))

# 粘贴第一张图片
img.paste(img1, box=(0, 0))
# 粘贴第二张图片
img.paste(img2, box=(img1.width, 0))

img.save("test.jpg")
img1.close()
img2.close()
