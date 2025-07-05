import pygame
import sys
import math

# 初始化pygame
pygame.init()

# 确保中文能正常显示
pygame.font.init()
font = pygame.font.SysFont(["SimHei", "WenQuanYi Micro Hei", "Heiti TC"], 24)

# 游戏窗口设置
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("车辆控制游戏")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 车辆属性
car_width = 30
car_height = 50
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 20
car_angle = 0  # 车辆朝向角度，0表示向上
speed = 5      # 前进后退速度
turn_speed = 3 # 转向速度

# 游戏主循环
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 清空屏幕
    screen.fill(WHITE)

    # 绘制边界
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT), 2)

    # 获取按键状态
    keys = pygame.key.get_pressed()
    
    # 初始化移动向量
    dx, dy = 0, 0
    
    # 处理上下键控制前进后退
    if keys[pygame.K_UP]:
        dy = -speed
    elif keys[pygame.K_DOWN]:
        dy = speed
    
    # 处理左右键控制转向（只有在前进或后退时才能转向）
    if (keys[pygame.K_UP] or keys[pygame.K_DOWN]):
        if keys[pygame.K_LEFT]:
            car_angle += turn_speed
        elif keys[pygame.K_RIGHT]:
            car_angle -= turn_speed
    
    # 确保角度在0-360度之间
    car_angle %= 360
    
    # 根据角度计算实际移动向量
    rad_angle = math.radians(car_angle)
    dx = dy * math.sin(rad_angle)
    dy = dy * math.cos(rad_angle)
    
    # 更新车辆位置
    car_x += dx
    car_y += dy
    
    # 边界检测，防止车辆驶出屏幕
    if car_x < 0:
        car_x = 0
    elif car_x > WIDTH - car_width:
        car_x = WIDTH - car_width
    
    if car_y < 0:
        car_y = 0
    elif car_y > HEIGHT - car_height:
        car_y = HEIGHT - car_height
    
    # 创建车辆矩形
    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    
    # 绘制车辆（带旋转效果）
    # 注意：Pygame的旋转是顺时针方向，所以我们使用负角度
    rotated_car = pygame.transform.rotate(
        pygame.Surface((car_width, car_height), pygame.SRCALPHA).convert_alpha(),
        -car_angle
    )
    rotated_car.fill(RED)
    screen.blit(rotated_car, (car_x, car_y))
    
    # 显示车辆角度信息
    angle_text = font.render(f"角度: {car_angle:.0f}°", True, BLACK)
    screen.blit(angle_text, (10, 10))
    
    # 显示操作提示
    control_text = font.render("↑↓:前进后退  ←→:转向", True, BLACK)
    screen.blit(control_text, (10, HEIGHT - 30))
    
    # 更新显示
    pygame.display.flip()
    
    # 控制帧率
    clock.tick(60)

# 退出游戏
pygame.quit()
sys.exit()
