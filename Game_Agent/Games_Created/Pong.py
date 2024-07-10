
import pygame
import pygame.font

# Initialize Pygame
pygame.init()
pygame.font.init()  # Initialize font module

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle dimensions
paddle_width = 10
paddle_height = 60

# Ball dimensions
ball_size = 10

# Paddle speed
paddle_speed = 0.2

# Ball speed
ball_x_speed = 0.1
ball_y_speed = 0.1

# Score
player1_score = 0
player2_score = 0

# Player 1 paddle position
player1_y = screen_height // 2 - paddle_height // 2

# Player 2 paddle position
player2_y = screen_height // 2 - paddle_height // 2

# Ball position
ball_x = screen_width // 2 - ball_size // 2
ball_y = screen_height // 2 - ball_size // 2

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player 1 controls
    keys = pygame.key.get_pressed()
    player1_y = max(0, min(player1_y + paddle_speed * (keys[pygame.K_s] - keys[pygame.K_w]), screen_height - paddle_height))

    # Player 2 controls
    player2_y = max(0, min(player2_y + paddle_speed * (keys[pygame.K_DOWN] - keys[pygame.K_UP]), screen_height - paddle_height))

    # Ball movement
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_y_speed *= -1

    # Ball collision with paddles (with margin)
    if ball_x <= paddle_width and ball_y + ball_size // 2 >= player1_y and ball_y + ball_size // 2 <= player1_y + paddle_height:
        ball_x_speed *= -1
    if ball_x >= screen_width - paddle_width - ball_size and ball_y + ball_size // 2 >= player2_y and ball_y + ball_size // 2 <= player2_y + paddle_height:
        ball_x_speed *= -1

    # Scoring (check for ball completely off-screen)
    if ball_x < 0:
        player2_score += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_x_speed *= -1
    if ball_x > screen_width:
        player1_score += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_x_speed *= -1

    # Clear the screen
    screen.fill(black)

    # Draw paddles
    player1_rect = pygame.Rect(0, player1_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, white, player1_rect)
    player2_rect = pygame.Rect(screen_width - paddle_width, player2_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, white, player2_rect)

    # Draw ball
    ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
    pygame.draw.rect(screen, white, ball_rect)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{player1_score} - {player2_score}", True, white)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
