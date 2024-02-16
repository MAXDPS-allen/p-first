import pygame
import random
import sys

# 初始化Pygame
pygame.init()

# 设置窗口尺寸和标题
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
WINDOW_TITLE = '随机音频播放器'
WINDOW_BG_COLOR = (255, 255, 255)  # 白色
FONT_COLOR = (0, 0, 0)  # 黑色
FONT_SIZE = 30
FONT_SIZE2 = 100

# 设置音频文件列表
AUDIO_FILES = ['A.mp3', 'B.mp3', 'C.mp3', 'D.mp3', 'E.mp3', 'F.mp3', 'G.mp3']

# 初始化窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# 初始化字体
font = pygame.font.Font(None, FONT_SIZE)
font2 = pygame.font.Font(None, FONT_SIZE2)


# 初始化音频
pygame.mixer.init()

def play_audio():
    audio_file = random.choice(AUDIO_FILES)
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    # 返回当前播放的音频文件名和对应的字母
    if audio_file == "A.mp3":
        return  "A"
    elif audio_file == "B.mp3":
        return  "B"
    elif audio_file == "C.mp3":
        return  "C"
    elif audio_file == "D.mp3":
        return  "D"
    elif audio_file == "E.mp3":
        return  "E"
    elif audio_file == "F.mp3":
        return  "F"
    elif audio_file == "G.mp3":
        return  "G"

# 创建滑块类
class Slider:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length
        self.handle_radius = 10
        self.value = 5
        self.dragging = False

    def draw(self, surface):
        pygame.draw.line(surface, FONT_COLOR, (self.x, self.y), (self.x + self.length, self.y), 2)
        pygame.draw.circle(surface, FONT_COLOR, (self.x + int(self.value / 10 * self.length), self.y), self.handle_radius)

    def update(self):
        if self.dragging:
            mouse_x, _ = pygame.mouse.get_pos()
            self.value = max(0, min(10, (mouse_x - self.x) / self.length * 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dist = ((self.x + int(self.value / 10 * self.length)) - mouse_x) ** 2 + (self.y - mouse_y) ** 2
            if dist <= self.handle_radius ** 2:
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

# 创建滑块实例
slider = Slider(50, 150, 300)

# 主程序
def main():
    interval = 2.5  # 初始播放间隔为2.5秒
    next_play_time = pygame.time.get_ticks() + interval * 2000
    play_audio()
    count = 0
    running = True
    while running:
        if count == 0:
            window.fill(WINDOW_BG_COLOR)
            count = count+1

        window.fill(WINDOW_BG_COLOR, (10, 125, 400, 50))

        current_time = pygame.time.get_ticks()

        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # 处理滑块事件
            slider.handle_event(event)

        # 更新滑块
        slider.update()

        # 绘制滑块
        slider.draw(window)

        # 更新窗口显示
        pygame.display.update()

        # 检查是否到达下一次播放时间
        if current_time >= next_play_time:

            window.fill(WINDOW_BG_COLOR, (270, 50, 200, 100))
            #pygame.display.update()
            current_letter = play_audio()  # 播放音频并获取对应的字母
            #print(text)
            text = font2.render(current_letter, True, FONT_COLOR)
            window.blit(text, (200 + 100 - text.get_width() / 2, 100 - text.get_height() / 2))
            pygame.display.update()
            
            next_play_time = current_time + int(slider.value) * 1000
            #play_audio()
            
            
           
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
