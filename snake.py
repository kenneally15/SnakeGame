import pygame
import random
import sys

# Initialize pygame
pygame.init()

# ----------------------------
# Game Configuration
# ----------------------------
WIDTH, HEIGHT = 600, 400       # Size of the game window
CELL_SIZE = 20                 # Size of each snake segment and food
FPS = 10                       # Frames per second (controls game speed)
FONT = pygame.font.SysFont("Arial", 25)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control game speed
clock = pygame.time.Clock()

def draw_text(text, color, x, y):
    """Utility function to draw text on the screen."""
    msg = FONT.render(text, True, color)
    screen.blit(msg, (x, y))

def main():
    # Initial snake position in the middle of the screen
    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2

    # Movement offsets (dx, dy)
    dx = CELL_SIZE
    dy = 0

    # List of snake segments, each element is [x, y]
    snake_body = [[snake_x, snake_y]]

    # Initial length of the snake
    snake_length = 3

    # Generate random position for the first food
    food_x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
    food_y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)

    score = 0
    game_over = False

    while True:
        # ----------------------------
        # EVENT HANDLING
        # ----------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # Change snake direction based on arrow keys or WASD
                if event.key in (pygame.K_LEFT, pygame.K_a) and dx == 0:
                    dx = -CELL_SIZE
                    dy = 0
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and dx == 0:
                    dx = CELL_SIZE
                    dy = 0
                elif event.key in (pygame.K_UP, pygame.K_w) and dy == 0:
                    dx = 0
                    dy = -CELL_SIZE
                elif event.key in (pygame.K_DOWN, pygame.K_s) and dy == 0:
                    dx = 0
                    dy = CELL_SIZE

        if not game_over:
            # ----------------------------
            # SNAKE MOVEMENT
            # ----------------------------
            snake_x += dx
            snake_y += dy

            # Add new head position to the front of snake_body
            snake_body.insert(0, [snake_x, snake_y])

            # If the snake hasn't eaten, remove the tail
            if len(snake_body) > snake_length:
                snake_body.pop()

            # ----------------------------
            # COLLISION DETECTION
            # ----------------------------
            # 1) Wall collision
            if (snake_x < 0 or snake_x >= WIDTH or
                snake_y < 0 or snake_y >= HEIGHT):
                game_over = True

            # 2) Self collision
            for segment in snake_body[1:]:
                if segment == [snake_x, snake_y]:
                    game_over = True

            # 3) Food collision
            if snake_x == food_x and snake_y == food_y:
                score += 1
                snake_length += 1
                # Spawn new food
                food_x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
                food_y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)

        # ----------------------------
        # RENDERING
        # ----------------------------
        screen.fill((0, 0, 0))  # Clear screen with black

        # Draw food
        pygame.draw.rect(screen, (255, 0, 0),
                         (food_x, food_y, CELL_SIZE, CELL_SIZE))

        # Draw snake
        for segment in snake_body:
            pygame.draw.rect(screen, (0, 255, 0),
                             (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

        # Display Score
        draw_text(f"Score: {score}", (255, 255, 255), 10, 10)

        if game_over:
            draw_text("GAME OVER", (255, 0, 0), WIDTH // 3, HEIGHT // 2)
            draw_text("Press any key to restart or close window to quit.",
                      (255, 255, 255), WIDTH // 15, HEIGHT // 2 + 40)
            pygame.display.update()

            # Wait for user input to restart or quit
            restart = True
            while restart:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        # Restart the game
                        main()

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

