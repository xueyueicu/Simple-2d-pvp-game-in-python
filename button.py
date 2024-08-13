import pygame


class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.text = text
        self.font = pygame.font.Font(None, 30)

    def is_hover(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        return self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height

    def draw(self, screen):
        is_hover = self.is_hover(pygame.mouse.get_pos())
        button_color = self.hover_color if is_hover else self.color
        pygame.draw.rect(screen, button_color, (self.x, self.y, self.width, self.height))
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.width/2, self.y + self.height/2)
        screen.blit(text_surface, text_rect)

    def handle_click(self, mouse_pos):
        if self.is_hover(mouse_pos):
            self.action()
            print("Button clicked")
            return True
        return False


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    button = Button("Click me", 100, 100, 100, 50, (255, 0, 0), (0, 255, 0), lambda: print("Button clicked"))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    button.handle_click(mouse_pos)

        screen.fill((255, 255, 255))  # 清屏
        button.draw(screen)  # 绘制按钮
        pygame.display.flip()  # 刷新显示

    pygame.quit()
