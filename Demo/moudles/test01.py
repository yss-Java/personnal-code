import pyecharts
# print(pyecharts.__version__)
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts

#得到折线图对象
line = Line()

#添加横坐标数据
line.add_xaxis(["中国","美国","日本"])

#添加纵坐标数据
line.add_yaxis("GDP",[30,20,10])
# 添加全局配置选项
line.set_global_opts(title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),  # 配置标题
                     legend_opts=LegendOpts(is_show=True),  # 配置图例，默认是展示的
                     toolbox_opts=ToolboxOpts(is_show=True),  # 配置工具箱
                     visualmap_opts=VisualMapOpts(is_show=True))  # 配置视觉映射

line.render()
