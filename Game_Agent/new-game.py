```python
import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake properties
snake_block_size = 10
snake_speed = 15

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Font for displaying score
font_style = pygame.font.SysFont(None, 30)

def display_score(score):
    """Renders the score on the screen."""
    value = font_style.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

def draw_snake(snake_block_size, snake_list):
    """Draws the snake on the screen."""
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, snake_block_size, snake_block_size])

def message(msg, color):
    """Displays a message on the screen."""
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/6, screen_height/3])

def game_loop():
    """The main game loop."""
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    # Food properties
    foodx = round(random.randrange(0, screen_width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block_size) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                    if event.key == pygame.K_c:
                        game_loop()
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Update snake's head position
        x1 += x1_change
        y1 += y1_change

        # Check for collisions
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        for x in snake_list[:-1]:
            if x == [x1, y1]:
                game_close = True

        # Add snake's head to the list
        snake_list.append([x1, y1])

        # Check if the snake has eaten food
        if len(snake_list) > snake_length:
            del snake_list[0] 

        # Draw the snake
        draw_snake(snake_block_size, snake_list)

        # Draw food
        pygame.draw.rect(screen, red, [foodx, foody, snake_block_size, snake_block_size])

        # Check if snake ate food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block_size) / 10.0) * 10.0
            snake_length += 1

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(snake_speed)

    # Quit Pygame
    pygame.quit()
    quit()

# Start the game
game_loop()
```