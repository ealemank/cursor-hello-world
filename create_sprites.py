import pygame
import os

# Initialize Pygame
pygame.init()

# Create assets directory if it doesn't exist
if not os.path.exists('assets'):
    os.makedirs('assets')

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

def create_player_sprite():
    surface = pygame.Surface((16, 16))
    surface.fill(BLACK)  # Transparent background
    # Draw body
    pygame.draw.rect(surface, BLUE, (4, 4, 8, 8))
    # Draw head
    pygame.draw.rect(surface, BLUE, (6, 2, 4, 4))
    # Draw legs
    pygame.draw.rect(surface, BLUE, (4, 12, 2, 4))
    pygame.draw.rect(surface, BLUE, (10, 12, 2, 4))
    return surface

def create_enemy_sprite():
    surface = pygame.Surface((16, 16))
    surface.fill(BLACK)  # Transparent background
    # Draw body
    pygame.draw.rect(surface, RED, (4, 4, 8, 8))
    # Draw head
    pygame.draw.rect(surface, RED, (6, 2, 4, 4))
    # Draw eyes
    pygame.draw.rect(surface, BLACK, (7, 3, 1, 1))
    pygame.draw.rect(surface, BLACK, (10, 3, 1, 1))
    return surface

def create_chest_sprite():
    surface = pygame.Surface((16, 16))
    surface.fill(BLACK)  # Transparent background
    # Draw chest body
    pygame.draw.rect(surface, GREEN, (2, 4, 12, 8))
    # Draw chest lid
    pygame.draw.rect(surface, GREEN, (2, 2, 12, 2))
    # Draw chest lock
    pygame.draw.rect(surface, BLACK, (7, 6, 2, 4))
    return surface

# Create and save sprites
pygame.image.save(create_player_sprite(), 'assets/player.png')
pygame.image.save(create_enemy_sprite(), 'assets/enemy.png')
pygame.image.save(create_chest_sprite(), 'assets/chest.png')

print("Sprites created successfully!") 