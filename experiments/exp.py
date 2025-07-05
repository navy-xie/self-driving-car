import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# 创建一个矩形 Surface
rect_surface = pygame.Surface((100, 50), pygame.SRCALPHA)
rect_surface.fill((255, 0, 0))  # 红色矩形

# 初始角度和位置
angle = 0
x, y = 200, 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle += 5
            elif event.key == pygame.K_RIGHT:
                angle -= 5

    screen.fill((0, 0, 0))
    
    # 旋转 Surface
    rotated_surface = pygame.transform.rotate(rect_surface, angle)
    rotated_rect = rotated_surface.get_rect(center=(x, y))
    
    # 绘制旋转后的矩形
    screen.blit(rotated_surface, rotated_rect)
    
    # 绘制中心点（便于观察）
    pygame.draw.circle(screen, (0, 255, 0), (x, y), 5)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
