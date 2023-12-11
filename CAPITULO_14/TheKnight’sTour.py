import pygame
import sys

class KnightTour:
    def __init__(self, n):
        self.n = n
        self.board = [[-1] * n for _ in range(n)]
        self.moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                      (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def is_valid_move(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.board[x][y] == -1

    def solve(self):
        return self._solve(0, 0, 1)

    def _solve(self, x, y, move_count):
        if move_count == self.n ** 2:
            return True

        for move in self.moves:
            new_x, new_y = x + move[0], y + move[1]
            if self.is_valid_move(new_x, new_y):
                self.board[new_x][new_y] = move_count
                if self._solve(new_x, new_y, move_count + 1):
                    return True
                self.board[new_x][new_y] = -1  # Backtrack

        return False

    def print_solution(self):
        for row in self.board:
            print(" ".join(map(lambda x: str(x).rjust(2), row)))

    def draw_board(self, screen, width, height):
        cell_size = min(width // self.n, height // self.n)

        for i in range(self.n):
            for j in range(self.n):
                pygame.draw.rect(screen, (255, 255, 255), (j * cell_size, i * cell_size, cell_size, cell_size), 2)
                if self.board[i][j] != -1:
                    text = font.render(str(self.board[i][j]), True, (0, 0, 0))
                    screen.blit(text, (j * cell_size + cell_size // 2 - 10, i * cell_size + cell_size // 2 - 10))

    def draw_knight(self, screen, width, height):
        cell_size = min(width // self.n, height // self.n)
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] != -1:
                    pygame.draw.circle(screen, (255, 0, 0), (j * cell_size + cell_size // 2, i * cell_size + cell_size // 2), 20)


# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Knight's Tour")

# Set up the font
pygame.font.init()
font = pygame.font.SysFont(None, 30)

# Create the KnightTour instance
n = 5
knight_tour = KnightTour(n)
knight_tour.solve()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    knight_tour.draw_board(screen, screen_width, screen_height)
    knight_tour.draw_knight(screen, screen_width, screen_height)
    pygame.display.flip()
