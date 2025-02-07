import streamlit as st
import pygame
import numpy as np
import time

# Initialize pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 400, 400
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

def draw_snake(snake_body, surface):
    for block in snake_body:
        pygame.draw.rect(surface, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

def main():
    st.title("Snake Game in Streamlit")
    st.write("Use arrow keys to play")

    canvas = st.empty()
    clock = pygame.time.Clock()

    # Initialize game variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [80, 50], [60, 50]]
    direction = 'RIGHT'
    change_to = direction
    food_pos = [np.random.randint(1, WIDTH//BLOCK_SIZE) * BLOCK_SIZE, 
                np.random.randint(1, HEIGHT//BLOCK_SIZE) * BLOCK_SIZE]
    food_spawn = True
    speed = 10
    
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
        
        # Ensuring the snake cannot reverse
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        
        # Move the snake
        if direction == 'UP':
            snake_pos[1] -= BLOCK_SIZE
        if direction == 'DOWN':
            snake_pos[1] += BLOCK_SIZE
        if direction == 'LEFT':
            snake_pos[0] -= BLOCK_SIZE
        if direction == 'RIGHT':
            snake_pos[0] += BLOCK_SIZE
        
        # Snake body growing
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            food_spawn = False
        else:
            snake_body.pop()
        
        if not food_spawn:
            food_pos = [np.random.randint(1, WIDTH//BLOCK_SIZE) * BLOCK_SIZE, 
                        np.random.randint(1, HEIGHT//BLOCK_SIZE) * BLOCK_SIZE]
        food_spawn = True
        
        # Game over conditions
        if snake_pos[0] < 0 or snake_pos[0] > WIDTH-BLOCK_SIZE or snake_pos[1] < 0 or snake_pos[1] > HEIGHT-BLOCK_SIZE:
            break
        for block in snake_body[1:]:
            if snake_pos == block:
                break
        
        # Render game
        surface = pygame.Surface((WIDTH, HEIGHT))
        surface.fill(BLACK)
        draw_snake(snake_body, surface)
        pygame.draw.rect(surface, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
        
        # Convert pygame surface to Streamlit image
        img = pygame.surfarray.array3d(surface)
        img = np.rot90(img)
        img = np.flipud(img)
        canvas.image(img, channels="RGB")
        
        clock.tick(speed)
        time.sleep(0.1)
    
    st.write("Game Over!")

if __name__ == "__main__":
    main()
