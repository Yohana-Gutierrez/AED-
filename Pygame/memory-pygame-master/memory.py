import os
import random
import time
import pygame

class MemoryGame:
    def __init__(self):
        pygame.init()
        self.SCREEN = (700, 600)
        self.ICON = pygame.image.load(os.path.join("memory.png"))
        pygame.display.set_icon(self.ICON)
        pygame.display.set_caption("Memory")
        self.DISPLAY = pygame.display.set_mode(self.SCREEN)

        # Define objects and generate number grid
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.ARIAL_200 = pygame.font.SysFont("Arial", 200)
        self.ARIAL_50 = pygame.font.SysFont("Arial", 50)
        self.ARIAL_35 = pygame.font.SysFont("Arial", 35)
        self.ARIAL_20 = pygame.font.SysFont("Arial", 20)
        self.CARD_LEN = 100
        self.CARD_MARGIN = 10
        self.CARD_HOR_PAD = 37
        self.CARD_VER_PAD = 22
        self.ROWS = 4 
        self.COLS = 5
        self.cards = [i for i in range(12) for j in range(2)]
        random.shuffle(self.cards)
        self.CARD_VAL_GRID = [self.cards[i * len(self.cards) // self.ROWS: (i + 1) * len(self.cards) // self.ROWS] for i in range(self.ROWS)]
        self.CARD_GRID = [[] for _ in range(self.ROWS)]
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if i == 0:
                    if j == 0:
                        self.CARD_GRID[i].append(pygame.Rect(self.CARD_MARGIN, self.CARD_MARGIN, self.CARD_LEN, self.CARD_LEN))
                    else:
                        self.CARD_GRID[i].append(pygame.Rect(self.CARD_GRID[i][j-1].x + self.CARD_LEN + self.CARD_MARGIN, self.CARD_MARGIN, self.CARD_LEN, self.CARD_LEN))
                else:
                    if j == 0:
                        self.CARD_GRID[i].append(pygame.Rect(self.CARD_MARGIN, self.CARD_GRID[i-1][0].y + self.CARD_LEN + self.CARD_MARGIN, self.CARD_LEN, self.CARD_LEN))
                    else:
                        self.CARD_GRID[i].append(pygame.Rect(self.CARD_GRID[i][j-1].x + self.CARD_LEN + self.CARD_MARGIN, self.CARD_GRID[i-1][0].y + self.CARD_LEN + self.CARD_MARGIN, self.CARD_LEN, self.CARD_LEN))

        self.exposed = []
        self.matched = []
        self.wrong = []
        self.turns = 0
        self.matched_label_timer = 5000  # Timer for displaying "Matched!"

        # Load music
        pygame.mixer.music.load(r"C:\Users\hammy\Music\musica.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for i in range(self.ROWS):
                        for j in range(self.COLS):
                            if self.CARD_GRID[i][j].collidepoint(mouse_pos):
                                has_instance = any(pos == [i, j] for pos in self.exposed) or any(pos == [i, j] for pos in self.matched)
                                if not has_instance:
                                    self.exposed.append([i, j])

            if len(self.exposed) == 2:
                self.turns += 1
                if all(0 <= pos[0] < self.ROWS and 0 <= pos[1] < self.COLS for pos in self.exposed):
                    if self.CARD_VAL_GRID[self.exposed[0][0]][self.exposed[0][1]] == self.CARD_VAL_GRID[self.exposed[1][0]][self.exposed[1][1]]:
                        # Display "Matched!" label
                        self.matched_label_timer = 60  # Show for 60 frames
                        self.matched.extend(self.exposed)
                        self.exposed.clear()
                    else:
                        self.wrong.extend(self.exposed)
                        self.exposed.clear()
                else:
                    self.exposed.clear()

            self.DISPLAY.fill(self.BLACK)

            for i in range(self.ROWS):
                for j in range(self.COLS):
                    pygame.draw.rect(self.DISPLAY, self.WHITE, self.CARD_GRID[i][j])

            if self.exposed:
                for i in self.exposed:
                    text = str(self.CARD_VAL_GRID[i[0]][i[1]])
                    render = self.ARIAL_50.render(text, True, self.BLACK)
                    self.DISPLAY.blit(render, (self.CARD_GRID[i[0]][i[1]].x + self.CARD_HOR_PAD, self.CARD_GRID[i[0]][i[1]].y + self.CARD_VER_PAD))

            if self.matched:
                for i in self.matched:
                    text = str(self.CARD_VAL_GRID[i[0]][i[1]])
                    render = self.ARIAL_50.render(text, True, self.GREEN)
                    self.DISPLAY.blit(render, (self.CARD_GRID[i[0]][i[1]].x + self.CARD_HOR_PAD, self.CARD_GRID[i[0]][i[1]].y + self.CARD_VER_PAD))

            if self.wrong:
                for i in self.wrong:
                    text = str(self.CARD_VAL_GRID[i[0]][i[1]])
                    render = self.ARIAL_50.render(text, True, self.RED)
                    self.DISPLAY.blit(render, (self.CARD_GRID[i[0]][i[1]].x + self.CARD_HOR_PAD, self.CARD_GRID[i[0]][i[1]].y + self.CARD_VER_PAD))

            if self.matched_label_timer > 0:
                matched_label = self.ARIAL_35.render("Matched!", True, self.GREEN)
                self.DISPLAY.blit(matched_label, (570, 150))
                self.matched_label_timer -= 1

            title = self.ARIAL_35.render("Memory", True, self.WHITE)
            self.DISPLAY.blit(title, (570, 10))
            turn_text = self.ARIAL_20.render("Turns: " + str(self.turns), True, self.WHITE)
            self.DISPLAY.blit(turn_text, (580, 75))

            if len(self.matched) == self.ROWS * self.COLS // 2:
                self.DISPLAY.fill(self.BLACK)
                win = self.ARIAL_200.render("You win!", True, self.GREEN)
                self.DISPLAY.blit(win, (40, 105))
                pygame.display.flip()
                time.sleep(2)
                pygame.quit()
                quit()

            pygame.display.flip()

            if self.wrong:
                time.sleep(1)
                self.wrong.clear()

if __name__ == "__main__":
    game = MemoryGame()
    game.run_game()
