# 人生重开模拟器
import random
import time
import sys

# 首先打印一个菜单栏
print('-----------------------------------------')
print('|            花有重开日，人无再少年          |')
print('|                                        |')
print('|            欢迎来到人生重开模拟器          |')
print('-----------------------------------------')

# 接下来，创建颜值，体质，智力，家境
# 这四个属性值都要在1-10之间，总和不要超过20

while True:
    print("请输入你的属性值")
    face = int(input("请输入你的颜值："))
    strong = int(input("请输入你的体质："))
    iq = int(input("请输入你的智商:"))
    home = int(input("请输入你的家境："))

    # 如果单个属性值超过10,提示用户重新输入
    if (face > 10 or face < 1):
        print("颜值输入错误，请重新输入")
        continue
    if (strong > 10 or strong < 1):
        print("体质输入错误，请重新输入")
        continue
    if (iq > 10 or iq < 1):
        print("智商输入错误，请重新输入")
        continue
    if (home > 10 or home < 1):
        print("家境输入错误，请重新输入")
        continue
    if (face + strong + iq + home > 20):
        print("属性值总和错误，请重新输入")
        continue
    print("颜值:", face, "体质:", strong, "智商:", iq, "家境:", home)
    break

# 接下来生成角色性别
# 使用random可以生成随机数
point = random.randint(1, 3)
if point == 1:
    gender = '男'
    print("你是男孩")
elif point == 2:
    gender = '女'
    print("你是一个女孩")
else:
    gender = '男娘'
    print("你是一个小男娘")

# 设置角色出生点
point = random.randint(1, 3)
if home == 10:
    # 第一档
    print("你出生在帝都，你的父母是高官政要")
    home += 1
    iq += 1
    face += 1
elif 7 <= home <= 9:
    # 第二档
    if point == 1:
        print("你出生在大城市，你父母是公务员")
        face += 2
    elif point == 2:
        print("你出生在大城市,你父母是企业高管")
        home += 2
    else:
        print("你出生在大城市，你父母是大学教授")
        iq += 2
elif 4 <= home <= 6:
    # 第三档
    if point == 1:
        print("你出生在三线城市，你父母是个体户")
        home += 1
    elif point == 2:
        print("你出生在三线城市,你父母是医生")
        face += 1
    else:
        print("你出生在三线城市，你父母是教师")
        iq += 1
else:
    # 第四档
    if point == 1:
        print("你出生在农村，你父母是农民")
        strong += 1
        face -= 2
    elif point == 2:
        print("你出生在穷乡僻壤,你父母是无业游民")
        home -= 1
    else:
        print("你出生在镇上，你父母感情不和")
        strong -= 1
print(f"当前的属性：颜值：{face},体质：{strong},智商:{iq},家境：{home}")

# 人生正式开始
# 幼年阶段
for age in range(1, 11):
    info = f'你今年{age}岁, '
    point = random.randint(1, 3)
    # 性别触发的事件
    if gender == 'girl' and home <= 3 and point == 1:
        info += '你的家里人重男轻女思想非常严重, 你被遗弃了!'
        print(info)
        print('游戏结束!')
        sys.exit(0)
        # 体制触发的事件
    elif strong < 6 and point < 3:
        info += '你生了一场病, '
        if home >= 5:
            info += '在父母的细心照料下, 你康复了'
            strong += 1
            home -= 1
        else:
            info += '你的父母没精力管你, 你的身体状况更遭了'
            strong -= 1
            # 颜值触发的事件
    elif face <= 4 and age >= 7:
        info += '你长得太丑了, 别的小朋友不喜欢你, '
        if iq > 5:
            info += '你决定用学习填充自己!'
            iq += 1
        else:
            if gender == 'boy':
                info += '你和别的小朋友经常打架!'
                strong += 1
                iq -= 1
            else:
                info += '你经常被别的小朋友欺负'
                strong -= 1
                # 智力触发的事件
    elif iq < 5:
        info += '你看起来傻傻的, '
        if home >= 7 and age >= 6:
            info += '你的父母把你送到更好的学校学习'
            iq += 1
        elif 4 <= home <= 6:
            if gender == 'boy':
                info += '你的父母鼓励你多运动, 争取成为运动员'
                strong += 1
            else:
                info += '你的父母鼓励你多打扮自己'
                face += 1
        else:
            info += '你的父母为此经常吵架'
            if point == 1:
                strong -= 1
            elif point == 2:
                iq -= 1
            else:
                pass
                # 健康成长事件
    else:
        info += '你健康成长, '
        if point == 1:
            info += '你看起来更结实了'
            strong += 1
        elif point == 2:
            info += '你看起来更好看了'
            face += 1
        else:
            info += '这一年没有特别的事情发生'
            # 打印这一年发生的事情
    print(info)
    print(f'颜值: {face}, 体质: {strong}, 智力: {iq}, 家境: {home}')
    print('---------------------------------------------')
    # 为了方便观察, 加一个sleep
time.sleep(2)

# 青年阶段
for age in range(11, 21):
    info = f'你今年{age}岁, '
    point = random.randint(1, 3)

    # 教育触发的事件
    if iq >= 7 and point == 1:
        info += '你在学校表现突出, 被选为班长!'
        if gender == 'boy':
            strong += 1
        else:
            face += 1
    elif iq < 5 and point == 2:
        info += '你的学习成绩不理想, 需要更多努力'
        if gender == 'boy':
            strong -= 1
        else:
            face -= 1

            # 职业选择事件
    elif age >= 16:
        if iq >= 8 and strong >= 7:
            info += '你的学业成就优秀, 获得了奖学金, 考上了理想的大学!'
            iq += 1
            strong += 1
        elif iq < 5 and strong < 5:
            info += '你无法考上理想的大学, 面临职业选择困难'
            if gender == 'boy':
                strong -= 1
            else:
                face -= 1
        else:
            info += '你选择了一份普通的工作, 开始了职业生涯'

            # 情感生活事件
    elif age >= 18:
        if point == 1:
            info += '你谈了一场甜蜜的恋爱, 与心爱的人交往中'
            if gender == 'boy':
                strong += 1
            else:
                face += 1
        elif point == 2:
            info += '你的恋爱关系出现了问题, 面临分手'
            if gender == 'boy':
                strong -= 1
            else:
                face -= 1

                # 健康成长事件
    else:
        info += '你在青年阶段健康成长, '
        if point == 1:
            info += '你继续保持健康的体魄'
            strong += 1
        elif point == 2:
            info += '你外貌更加成熟美好'
            face += 1
        else:
            info += '这一阶段没有特别的事情发生'

            # 打印这一年发生的事情
    print(info)
    print(f'颜值: {face}, 体制: {strong}, 智力: {iq}, 家境: {home}')
    print('---------------------------------------------')
    # 加入延迟以模拟事件发生
    time.sleep(2)

# 中年阶段
for age in range(21, 61):
    info = f'你今年{age}岁, '
    point = random.randint(1, 3)
    # 职业发展事件
    if age >= 21 and age <= 40:
        if iq >= 8 and strong >= 7:
            info += '你在职场上取得了显著成就, 获得了晋升!'
            iq += 1
            strong += 1
            home += 1
        elif iq < 5 and strong < 5:
            info += '你在职场上遇到了挑战, 需要调整策略'
            iq -= 1
            strong -= 1
            home -= 1
        else:
            info += '你的职业生涯稳步发展'

            # 家庭生活事件
    elif age >= 25:
        if point == 1:
            info += '你的家庭生活幸福美满'
            home += 1
        elif point == 2:
            info += '你的家庭出现了一些小矛盾, 需要沟通解决'
            home -= 1

            # 健康问题
    if age > 40:
        if point == 1:
            info += '你开始注重健康, 定期进行体检'
            strong += 1
        elif point == 2:
            info += '你遇到了健康问题, 需要及时治疗'
            strong -= 1

            # 退休生活准备
    if age >= 55:
        info += '你开始考虑退休生活, 准备享受晚年'
        home += 1

        # 打印这一年发生的事情
    print(info)
    print(f'颜值: {face}, 体制: {strong}, 智力: {iq}, 家境: {home}')
    print('---------------------------------------------')
    # 加入延迟以模拟事件发生
    time.sleep(2)

# 晚年阶段
for age in range(61, 81):
    info = f'你今年{age}岁, '
    point = random.randint(1, 3)

    # 退休生活事件
    if age >= 61:
        if point == 1:
            info += '你开始享受退休生活, 生活变得悠闲'
            home += 1
        elif point == 2:
            info += '你开始感到无聊, 需要找点事情做'
            home -= 1

            # 健康问题
    if age > 70:
        if point == 1:
            info += '你开始注重健康, 定期进行体检'
            strong += 1
        elif point == 2:
            info += '你遇到了健康问题, 需要及时治疗'
            strong -= 1

            # 打印这一年发生的事情
    print(info)
    print(f'颜值: {face}, 体制: {strong}, 智力: {iq}, 家境: {home}')
    print('---------------------------------------------')
    print("你这一生结束了")
    print(f'颜值: {face}, 体制: {strong}, 智力: {iq}, 家境: {home}')
    # 加入延迟以模拟事件发生
    time.sleep(2)
