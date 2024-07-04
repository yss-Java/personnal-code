old_name = input('请输入你要备份的文件的名称：')
# 从后往前找，找到的第一个.的位置就是最后一个.的位置
index = old_name.rfind('.')
if index > 0:
    #判断文件名的合法性
    postfix = old_name[index:]
new_name=old_name[:index]+'[备份]'+postfix
# 组合成新的备份文件名

# 打开原文件，并创建备份文件
old_f = open(old_name,'r')
new_f = open(new_name,'w')

while True:
    con = old_f.read(1024)
    if len(con) == 0:  # 当读取的内容长度为0时，表明原文件内容已读取完
        break
    new_f.write(con)




