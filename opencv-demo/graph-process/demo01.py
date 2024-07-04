from PIL import Image

# 缩小一半, 然后水平翻转, 然后旋转45度并向右平移一段距离
with Image.open("D:\project\images\img2.jpg") as img:
    print(img.mode)

    # 缩小一半
    img = img.resize((img.width // 2, img.height // 2))

    # 水平翻转
    img = img.transpose(Image.FLIP_LEFT_RIGHT)

    # 旋转45度, 扩展输出图片大小(内切), 向右平移50像素, 旋转后的空白区域使用灰色填充
    img = img.rotate(45, expand=True, translate=(10, 0), fillcolor="#888888")

    img.save("img2_out.jpg")
