import pygame
import random

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# 테트로미노 모양과 색상
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

COLORS = [
    (0, 255, 255), (255, 255, 0), (128, 0, 128),
    (255, 165, 0), (0, 0, 255), (0, 255, 0), (255, 0, 0)
]

# 게임 설정
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SCREEN_WIDTH = BOARD_WIDTH * BLOCK_SIZE
SCREEN_HEIGHT = BOARD_HEIGHT * BLOCK_SIZE

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('테트리스')
        self.clock = pygame.time.Clock()
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.fall_time = 0
        self.fall_speed = 0.5
        self.lock_time = 0
        self.lock_delay = 0.5

    def new_piece(self):
        shape = random.choice(SHAPES)
        color = random.choice(COLORS)
        return {
            'shape': shape,
            'color': color,
            'x': BOARD_WIDTH // 2 - len(shape[0]) // 2,
            'y': 0
        }

    def valid_move(self, piece, x, y):
        for i, row in enumerate(piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    if (x + j < 0 or x + j >= BOARD_WIDTH or
                        y + i >= BOARD_HEIGHT or
                        (y + i >= 0 and self.board[y + i][x + j])):
                        return False
        return True

    def add_to_board(self, piece):
        for i, row in enumerate(piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    self.board[piece['y'] + i][piece['x'] + j] = piece['color']

    def remove_full_rows(self):
        full_rows = [i for i, row in enumerate(self.board) if all(row)]
        for row in full_rows:
            del self.board[row]
            self.board.insert(0, [0 for _ in range(BOARD_WIDTH)])
        return len(full_rows)

    def rotate_piece(self, piece):
        return {
            'shape': list(zip(*piece['shape'][::-1])),
            'color': piece['color'],
            'x': piece['x'],
            'y': piece['y']
        }

    def draw(self):
        self.screen.fill(BLACK)
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, cell,
                                     (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1))

        if self.current_piece:
            for i, row in enumerate(self.current_piece['shape']):
                for j, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(self.screen, self.current_piece['color'],
                                         ((self.current_piece['x'] + j) * BLOCK_SIZE,
                                          (self.current_piece['y'] + i) * BLOCK_SIZE,
                                          BLOCK_SIZE - 1, BLOCK_SIZE - 1))

        score_text = self.font.render(f'점수: {self.score}', True, WHITE)
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            game_over_text = self.font.render('게임 오버!', True, WHITE)
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 70, SCREEN_HEIGHT // 2 - 30))

        pygame.display.flip()

    def run(self):
        while not self.game_over:
            self.fall_time += self.clock.get_rawtime() / 1000
            self.clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.valid_move(self.current_piece, self.current_piece['x'] - 1, self.current_piece['y']):
                            self.current_piece['x'] -= 1
                            self.lock_time = 0
                    elif event.key == pygame.K_RIGHT:
                        if self.valid_move(self.current_piece, self.current_piece['x'] + 1, self.current_piece['y']):
                            self.current_piece['x'] += 1
                            self.lock_time = 0
                    elif event.key == pygame.K_DOWN:
                        if self.valid_move(self.current_piece, self.current_piece['x'], self.current_piece['y'] + 1):
                            self.current_piece['y'] += 1
                            self.lock_time = 0
                    elif event.key == pygame.K_UP:
                        rotated_piece = self.rotate_piece(self.current_piece)
                        if self.valid_move(rotated_piece, rotated_piece['x'], rotated_piece['y']):
                            self.current_piece = rotated_piece
                            self.lock_time = 0

            if self.fall_time > self.fall_speed:
                if self.valid_move(self.current_piece, self.current_piece['x'], self.current_piece['y'] + 1):
                    self.current_piece['y'] += 1
                    self.lock_time = 0
                else:
                    self.lock_time += self.fall_time
                    if self.lock_time > self.lock_delay:
                        self.add_to_board(self.current_piece)
                        rows_cleared = self.remove_full_rows()
                        self.score += rows_cleared * 100
                        self.current_piece = self.new_piece()
                        if not self.valid_move(self.current_piece, self.current_piece['x'], self.current_piece['y']):
                            self.game_over = True
                        self.lock_time = 0
                self.fall_time = 0

            self.draw()

        pygame.quit()

if __name__ == '__main__':
    Tetris().run()