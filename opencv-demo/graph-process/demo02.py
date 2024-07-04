from PIL import Image, ImageFilter

with Image.open("D:\project\images\img2.jpg") as img:
    # gray_img = img.convert('L')
    # gray_img.save("img2_gray.jpg")
    # 浮雕 过滤器
    # emboss_img = img.filter(ImageFilter.EMBOSS)
    # emboss_img.save("img2_emboss.jpg")

    # 轮廓 过滤器
    # contour_img=img.filter(ImageFilter.CONTOUR)
    # contour_img.save("img2_contour.jpg")

    # 寻找边缘 过滤器
    # find_edges_img = img.filter(ImageFilter.FIND_EDGES)
    # find_edges_img.save("img2_find_edges.jpg")

    #边缘增强 过滤器
    edge_enhance_img=img.filter(ImageFilter.EDGE_ENHANCE)
    edge_enhance_img.save("img2_find_edge_enhance.jpg")


