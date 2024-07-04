# 编写一个Python程序，实现一个眨眼的动画效果。该动画效果应该在屏幕上显示一个人脸，并在一定的时间间隔内使眼睛闭合和睁开。
import pygame
import time

pygame.init()
# 设置窗口大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# 设置颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# 设置人脸参数
face_width = 200
face_height = 200
face_x = screen_width // 2 - face_width // 2
face_y = screen_height // 2 - face_height // 2
# 设置眼睛参数
eye_width = 20
eye_height = 10
eye_offset = 30
# 设置嘴巴参数
mouth_width = 60
mouth_height = 20
mouth_offset = 70
# 设置动画参数
blink_duration = 0.5  # 眨眼动画持续时间（秒）
blink_interval = 3  # 眨眼间隔时间（秒）
mouth_open_duration = 0.5  # 嘴巴张开动画持续时间（秒）
mouth_interval = 2  # 嘴巴动画间隔时间（秒）
# 初始化时钟
clock = pygame.time.Clock()
running = True
blink_time = 0
mouth_time = 0
blink = False
mouth_open = False
while running:
    screen.fill(WHITE)
    # 绘制人脸
    pygame.draw.ellipse(screen, BLACK, (face_x, face_y, face_width, face_height))
    # 绘制眼睛
    if blink:
        # 眨眼
        pygame.draw.ellipse(screen, WHITE, (face_x + eye_offset, face_y + eye_offset, eye_width, eye_height))
        pygame.draw.ellipse(screen, WHITE,
                            (face_x + face_width - eye_offset - eye_width, face_y + eye_offset, eye_width, eye_height))
    else:
        # 正常眼睛
        pygame.draw.ellipse(screen, BLACK, (face_x + eye_offset, face_y + eye_offset, eye_width, eye_height))
        pygame.draw.ellipse(screen, BLACK,
                            (face_x + face_width - eye_offset - eye_width, face_y + eye_offset, eye_width, eye_height))
    # 绘制嘴巴
    if mouth_open:
        # 张开嘴巴
        pygame.draw.ellipse(screen, WHITE,
                            (face_x + mouth_offset, face_y + mouth_offset * 2, mouth_width, mouth_height))

    else:
        # 闭嘴
        pygame.draw.ellipse(screen, BLACK,
                            (face_x + mouth_offset, face_y + mouth_offset * 2, mouth_width, mouth_height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 更新眨眼动画
    current_time = time.time()
    if current_time - blink_time > blink_interval:
        blink = not blink
        blink_time = current_time
    if blink and current_time - blink_time > blink_duration:
        blink = False
    # 更新嘴巴动画
    if current_time - mouth_time > mouth_interval:
        mouth_open = True
        mouth_time = current_time
    if mouth_open and current_time - mouth_time > mouth_open_duration:
        mouth_open = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

