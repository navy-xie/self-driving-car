import pygame
import math

# 初始化pygame
pygame.init()

# 设置窗口大小
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("车辆模拟")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 车辆参数
car_width = 30
car_height = 50
car_x = screen_width // 2 - car_width // 2
car_y = screen_height - car_height - 20
car_speed = 0
car_max_speed = 5
car_acceleration = 0.1
car_deceleration = 0.2
car_angle = 0  # 角度，0表示向上
car_turning_speed = 2  # 转向速度（度/帧）

# 游戏主循环
clock = pygame.time.Clock()
running = True

while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 获取按键状态
    keys = pygame.key.get_pressed()
    
    # 处理车辆运动
    # 前进/后退
    if keys[pygame.K_UP]:
        car_speed += car_acceleration
        if car_speed > car_max_speed:
            car_speed = car_max_speed
    elif keys[pygame.K_DOWN]:
        car_speed -= car_acceleration
        if car_speed < -car_max_speed / 2:  # 倒车速度较慢
            car_speed = -car_max_speed / 2
    else:
        # 没有按键时减速
        if car_speed > 0:
            car_speed -= car_deceleration
            if car_speed < 0:
                car_speed = 0
        elif car_speed < 0:
            car_speed += car_deceleration
            if car_speed > 0:
                car_speed = 0
    
    # 转向 - 只有在移动时才能转向
    if abs(car_speed) > 0.1:  # 很小的速度时不转向
        if keys[pygame.K_LEFT]:
            car_angle += car_turning_speed
        if keys[pygame.K_RIGHT]:
            car_angle -= car_turning_speed
    
    # 更新车辆位置
    angle_rad = math.radians(car_angle)
    car_x += car_speed * math.sin(angle_rad)
    car_y -= car_speed * math.cos(angle_rad)
    
    # 边界检查
    if car_x < 0:
        car_x = 0
    elif car_x > screen_width - car_width:
        car_x = screen_width - car_width
    
    if car_y < 0:
        car_y = 0
    elif car_y > screen_height - car_height:
        car_y = screen_height - car_height
    
    # 绘制
    screen.fill(BLACK)
    
    # 绘制车辆（旋转的矩形）
    car_surface = pygame.Surface((car_width, car_height), pygame.SRCALPHA)
    pygame.draw.rect(car_surface, RED, (0, 0, car_width, car_height))
    rotated_car = pygame.transform.rotate(car_surface, car_angle)
    car_rect = rotated_car.get_rect(center=(car_x + car_width // 2, car_y + car_height // 2))
    screen.blit(rotated_car, car_rect.topleft)
    
    # 更新显示
    pygame.display.flip()
    
    # 控制帧率
    clock.tick(60)

pygame.quit()
