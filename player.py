import pygame
import color

class Player():
    def __init__(self):
        self.x = 500
        self.y = 400

        self.moveX = 0
        self.moveY = 0

        self.mousePos = pygame.mouse.get_pos()

    def draw(self, surface):
        pygame.draw.circle(surface, color.WHITE, (self.x, self.y), 10.0)

        pygame.draw.line(surface, color.RED, (self.x, self.y), (self.mousePos[0], self.mousePos[1]), 3)

    def update(self, events):
        self.x += self.moveX
        self.y += self.moveY

        self.movementHandler(events)

        self.mousePos = pygame.mouse.get_pos()

    def movementHandler(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.moveX = 5
                if event.key == pygame.K_a:
                    self.moveX = -5

                if event.key == pygame.K_w:
                    self.moveY = -5
                if event.key == pygame.K_s:
                    self.moveY = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    self.moveX = 0
                
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.moveY = 0
