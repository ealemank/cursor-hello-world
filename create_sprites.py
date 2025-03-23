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
BROWN = (139, 69, 19)
SKIN_COLOR = (255, 218, 185)
GOLD = (255, 215, 0)
DARK_BROWN = (101, 67, 33)

def create_player_sprite():
    surface = pygame.Surface((16, 16))
    surface.fill(BLACK)  # Transparent background
    
    # Draw body (green tunic)
    pygame.draw.rect(surface, GREEN, (4, 6, 8, 8))
    
    # Draw head
    pygame.draw.rect(surface, SKIN_COLOR, (6, 2, 4, 4))
    
    # Draw hair (blonde)
    pygame.draw.rect(surface, GOLD, (5, 1, 6, 1))
    pygame.draw.rect(surface, GOLD, (4, 2, 8, 1))
    
    # Draw legs (brown pants)
    pygame.draw.rect(surface, BROWN, (4, 14, 2, 2))
    pygame.draw.rect(surface, BROWN, (10, 14, 2, 2))
    
    # Draw boots
    pygame.draw.rect(surface, DARK_BROWN, (3, 15, 2, 1))
    pygame.draw.rect(surface, DARK_BROWN, (11, 15, 2, 1))
    
    # Draw belt
    pygame.draw.rect(surface, BROWN, (4, 13, 8, 1))
    
    return surface

def create_enemy_sprite():
    surface = pygame.Surface((16, 16))
    surface.fill(BLACK)  # Transparent background
    
    # Draw body (red tunic)
    pygame.draw.rect(surface, RED, (4, 6, 8, 8))
    
    # Draw head (green skin)
    pygame.draw.rect(surface, (0, 100, 0), (6, 2, 4, 4))
    
    # Draw ears (pointed)
    pygame.draw.rect(surface, (0, 100, 0), (4, 2, 2, 3))
    pygame.draw.rect(surface, (0, 100, 0), (10, 2, 2, 3))
    
    # Draw eyes (yellow)
    pygame.draw.rect(surface, (255, 255, 0), (7, 3, 1, 1))
    pygame.draw.rect(surface, (255, 255, 0), (10, 3, 1, 1))
    
    # Draw legs
    pygame.draw.rect(surface, BROWN, (4, 14, 2, 2))
    pygame.draw.rect(surface, BROWN, (10, 14, 2, 2))
    
    # Draw boots
    pygame.draw.rect(surface, DARK_BROWN, (3, 15, 2, 1))
    pygame.draw.rect(surface, DARK_BROWN, (11, 15, 2, 1))
    
    return surface

def create_chest_sprite():
    surface = pygame.Surface((16, 16))
    surface.fill(BLACK)  # Transparent background
    
    # Draw chest body (wooden)
    pygame.draw.rect(surface, BROWN, (2, 6, 12, 6))
    
    # Draw chest lid
    pygame.draw.rect(surface, DARK_BROWN, (2, 2, 12, 4))
    
    # Draw chest details (wooden planks)
    pygame.draw.rect(surface, DARK_BROWN, (4, 6, 1, 6))  # Left plank
    pygame.draw.rect(surface, DARK_BROWN, (11, 6, 1, 6))  # Right plank
    pygame.draw.rect(surface, DARK_BROWN, (2, 8, 12, 1))  # Middle plank
    
    # Draw chest lock
    pygame.draw.rect(surface, GOLD, (7, 6, 2, 4))
    pygame.draw.rect(surface, DARK_BROWN, (7, 6, 2, 1))  # Lock top
    
    # Draw chest hinges
    pygame.draw.rect(surface, DARK_BROWN, (4, 2, 1, 2))
    pygame.draw.rect(surface, DARK_BROWN, (11, 2, 1, 2))
    
    return surface

# Create and save sprites
pygame.image.save(create_player_sprite(), 'assets/player.png')
pygame.image.save(create_enemy_sprite(), 'assets/enemy.png')
pygame.image.save(create_chest_sprite(), 'assets/chest.png')

print("Sprites created successfully!") 