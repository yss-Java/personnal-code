import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# my_font = fm.FontProperties(fname='C:/Windows/Fonts/SimHei.ttf')
x=[1,2,3,4,5]
y=[10,8,6,4,2]
# plt.plot(x,y)
matplotlib.rcParams['font.family']='SimHei'
# plt.title('折线图示例',fontproperties=my_font)
# plt.xlabel('X轴',fontproperties=my_font)
# plt.ylabel('Y轴',fontproperties=my_font)
# plt.show()
# fig, axs = plt.subplots(2, 2)
#
# axs[0, 0].plot(x, y)
# axs[0, 0].set_title('子图1')
# axs[0, 1].scatter(x, y)
# axs[0, 1].set_title('子图2')
# axs[1, 0].bar(x, y)
# axs[1, 0].set_title('子图3')
# axs[1, 1].pie(y)
# axs[1, 1].set_title('子图4')
#
# plt.show()

plt.plot(x, y)
plt.title('折线图示例')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.savefig('D:\\springboot\\download\\line_chart.png')
