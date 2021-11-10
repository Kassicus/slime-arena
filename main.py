import pygame
import color

pygame.init()

class Game():
    def __init__(self):
        self.WIDTH = 1000
        self.HEIGHT = 800
        self.TITLE = "Slime Arena"

        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption(self.TITLE)

        self.running = False
        self.clock = pygame.time.Clock()

        self.events = pygame.event.get()

    def start(self):
        self.running = True

        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(color.BLACK)

    def update(self):
        pygame.display.update()
        self.clock.tick(30)

game = Game()
game.start()

pygame.quit()
