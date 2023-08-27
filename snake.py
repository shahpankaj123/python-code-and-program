import pygame
import random

# Initialize Pygame
pygame.init()

# Set the game window dimensions
width = 640
height = 480

# Create the game window
screen = pygame.display.set_mode((width, height))

# Set the font for the game over message
font = pygame.font.SysFont('Arial', 72)

# Set the colors used in the game
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Set the size of the snake's segments and the space between them
segment_size = 10
segment_margin = 2

# Set the starting position of the snake
snake_segments = [(50, 50), (40, 50), (30, 50)]
snake_direction = "right"

# Set the initial position of the food
food_position = (random.randint(0, width - segment_size), random.randint(0, height - segment_size))

# Set the initial score
score = 0

# Set the clock for the game
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT:
                snake_direction = "right"
            elif event.key == pygame.K_UP:
                snake_direction = "up"
            elif event.key == pygame.K_DOWN:
                snake_direction = "down"

    # Move the snake
    if snake_direction == "right":
        snake_segments.insert(0, (snake_segments[0][0] + segment_size, snake_segments[0][1]))
    elif snake_direction == "left":
        snake_segments.insert(0, (snake_segments[0][0] - segment_size, snake_segments[0][1]))
    elif snake_direction == "up":
        snake_segments.insert(0, (snake_segments[0][0], snake_segments[0][1] - segment_size))
    elif snake_direction == "down":
        snake_segments.insert(0, (snake_segments[0][0], snake_segments[0][1] + segment_size))

    # Check for collisions with the food
    if snake_segments[0] == food_position:
        food_position = (random.randint(0, width - segment_size), random.randint(0, height - segment_size))
        score += 10
    else:
        snake_segments.pop()

    # Check for collisions with the walls or with the snake's body
    if snake_segments[0][0] < 0 or snake_segments[0][0] >= width or snake_segments[0][1] < 0 or snake_segments[0][1] >= height:
        game_over_message = font.render("Game Over", True, white)
        screen.blit(game_over_message, (width/2 - game_over_message.get_width()/2, height/2 - game_over_message.get_height()/2))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        quit()
    for segment in snake_segments[1:]:
        if snake_segments[0] == segment:
            game_over_message = font.render("Game Over", True, white)
            screen.blit(game_over_message, (width/2 - game_over_message.get_width()/2, height/2 - game_over_message.get_height()/
        2))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        quit()

# Draw the screen
screen.fill(black)
pygame.draw.rect(screen, green, (food_position[0], food_position[1], segment_size, segment_size))
for segment in snake_segments:
    pygame.draw.rect(screen, white, (segment[0], segment[1], segment_size, segment_size))

# Draw the score
score_message = font.render("Score: " + str(score), True, white)
screen.blit(score_message, (10, 10))

# Update the display
pygame.display.update()

# Set the game speed
clock.tick(10)
