import pygame
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()

class dot: 
    def __init__(self, screen): 
        self.screen = screen
        self.ball = 0
        self.x = 960
        self.y = 540

    def create(self):
        pygame.draw.circle(screen, (255, 0, 0), [self.x, self.y], 5)

    def get_display_x(self):
        start = 960
        x = (self.x - start) / 20
        return x

    def get_display_y(self):
        start = 540
        y = (start - self.y) / 20
        return y


screen_width = 1920 # 가로 길이
screen_height = 1080 # 세로 길이
screen = pygame.display.set_mode((screen_width, screen_height)) # 창 생성

pygame.display.set_caption("Shape Movement") # 창 제목 설정

clock = pygame.time.Clock()

background = pygame.image.load(resource_path("image\\coord.png"))

text_font = pygame.font.Font(None, 25)

dot = dot(screen)

running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if dot.x - 10 > 0:
                    dot.x -= 10
            elif event.key == pygame.K_RIGHT: 
                if dot.x + 10 < screen_width:
                    dot.x += 10
            elif event.key == pygame.K_UP:
                if dot.y - 10 > 0:
                    dot.y -= 10
            elif event.key == pygame.K_DOWN:
                if dot.y + 10 < screen_height:
                    dot.y += 10

    screen.blit(background, (0, 0))

    dot.create()

    pos_text = text_font.render("({}, {})".format(dot.get_display_x(), dot.get_display_y()), True, (0, 255, 0))
    screen.blit(pos_text, (dot.x - 40, dot.y - 25))

    pygame.display.update()
    
pygame.quit()