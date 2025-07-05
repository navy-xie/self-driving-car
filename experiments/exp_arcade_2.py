import arcade
import math

# 窗口设置
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "车辆模拟器"

# 车辆参数
CAR_SPEED = 5  # 基础速度
TURN_SPEED = 3  # 转向速度（角度/帧）

class CarSimulation(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # 设置背景色（灰色路面）
        arcade.set_background_color(arcade.color.DARK_GRAY)
        
        # 加载车辆精灵（可替换为自己的图片，如 car.png）
        self.car = arcade.Sprite("../car.png", scale=0.5)  # scale 调整大小
        # 初始位置：屏幕中心
        self.car.center_x = SCREEN_WIDTH / 2
        self.car.center_y = SCREEN_HEIGHT / 2
        # 初始角度：向上（0度为右，90度为上，可根据图片方向调整）
        self.car.angle = 90

        # 存储按键状态
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def on_key_press(self, key, modifiers):
        """处理按键按下事件"""
        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True

    def on_key_release(self, key, modifiers):
        """处理按键释放事件"""
        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
        elif key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False

    def on_update(self, delta_time):
        """每帧更新车辆状态（delta_time 为帧间隔时间）"""
        
        # 前进（上键）：沿当前角度移动
        if self.up_pressed:
            # 计算角度对应的x、y方向增量（三角函数）
            angle_rad = math.radians(self.car.angle)
            self.car.center_x += math.cos(angle_rad) * CAR_SPEED
            self.car.center_y += math.sin(angle_rad) * CAR_SPEED
        
        # 后退（下键）：沿当前角度反向移动
        if self.down_pressed:
            angle_rad = math.radians(self.car.angle)
            self.car.center_x -= math.cos(angle_rad) * CAR_SPEED
            self.car.center_y -= math.sin(angle_rad) * CAR_SPEED
        
        # 左转（左键）：减小角度（逆时针转）
        if self.left_pressed:
            self.car.angle -= TURN_SPEED
        
        # 右转（右键）：增大角度（顺时针转）
        if self.right_pressed:
            self.car.angle += TURN_SPEED
        
        # 限制车辆在窗口内（可选）
        self.car.center_x = max(0, min(self.car.center_x, SCREEN_WIDTH))
        self.car.center_y = max(0, min(self.car.center_y, SCREEN_HEIGHT))

    def on_draw(self):
        """绘制画面"""
        arcade.start_render()  # 开始渲染
        self.car.draw()  # 绘制车辆

if __name__ == "__main__":
    # 启动游戏
    window = CarSimulation()
    arcade.run()