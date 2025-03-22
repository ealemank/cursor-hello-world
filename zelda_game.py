import pygame
import random
import math
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('game.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 32
PLAYER_SPEED = 5
ENEMY_SPEED = 2
SWORD_RANGE = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Load images
def load_image(name, scale=2):
    try:
        logger.debug(f"Attempting to load image: {name}")
        image_path = os.path.join('assets', name)
        logger.debug(f"Full image path: {image_path}")
        logger.debug(f"File exists: {os.path.exists(image_path)}")
        
        image = pygame.image.load(image_path)
        logger.info(f"Successfully loaded image: {name}")
        logger.debug(f"Original image size: {image.get_width()}x{image.get_height()}")
        
        if scale != 1:
            new_size = (image.get_width() * scale, image.get_height() * scale)
            logger.debug(f"Scaling image to: {new_size}")
            image = pygame.transform.scale(image, new_size)
        return image
    except Exception as e:
        logger.error(f"Error loading image {name}: {str(e)}")
        # Create a colored surface if image loading fails
        surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
        if name == 'player.png':
            surface.fill(BLUE)
        elif name == 'enemy.png':
            surface.fill(RED)
        elif name == 'chest.png':
            surface.fill(GREEN)
        return surface

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_image('player.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.has_sword = True
        self.attacking = False
        self.attack_cooldown = 0
        self.facing_right = True
        self.original_image = self.image

    def move(self, dx, dy):
        self.rect.x += dx * PLAYER_SPEED
        self.rect.y += dy * PLAYER_SPEED
        # Keep player on screen
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())
        
        # Update facing direction
        if dx > 0:
            self.facing_right = True
        elif dx < 0:
            self.facing_right = False
            
        # Flip image based on direction
        if not self.facing_right:
            self.image = pygame.transform.flip(self.original_image, True, False)
        else:
            self.image = self.original_image

    def attack(self):
        if self.has_sword and self.attack_cooldown <= 0:
            self.attacking = True
            self.attack_cooldown = 30

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_image('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 50
        self.speed = ENEMY_SPEED
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.original_image = self.image
        self.facing_right = True

    def update(self, player):
        # Move towards player
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y
        dist = math.sqrt(dx**2 + dy**2)
        if dist != 0:
            self.rect.x += (dx/dist) * self.speed
            self.rect.y += (dy/dist) * self.speed
            
            # Update facing direction
            if dx > 0:
                self.facing_right = True
            else:
                self.facing_right = False
                
            # Flip image based on direction
            if not self.facing_right:
                self.image = pygame.transform.flip(self.original_image, True, False)
            else:
                self.image = self.original_image

class Chest(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_image('chest.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.opened = False
        self.original_image = self.image

    def open(self):
        if not self.opened:
            self.opened = True
            # Here you could load an opened chest image if you had one
            # self.image = load_image('chest_open.png')

class Game:
    def __init__(self):
        logger.info("Initializing game...")
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Zelda-like Dungeon")
        self.clock = pygame.time.Clock()
        self.running = True
        self.setup_game()
        logger.info("Game initialized successfully")

    def setup_game(self):
        logger.debug("Setting up game objects...")
        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        # Create player
        self.player = Player(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
        self.all_sprites.add(self.player)
        logger.debug("Player created and added to sprites")
        
        # Create enemies
        for i in range(5):
            enemy = Enemy(random.randint(0, WINDOW_WIDTH-TILE_SIZE),
                         random.randint(0, WINDOW_HEIGHT-TILE_SIZE))
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
        logger.debug(f"Created {len(self.enemies)} enemies")
        
        # Create chest
        self.chest = Chest(WINDOW_WIDTH-100, WINDOW_HEIGHT-100)
        self.all_sprites.add(self.chest)
        logger.debug("Chest created and added to sprites")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logger.info("Quit event received")
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    logger.debug("Space key pressed - player attacking")
                    self.player.attack()

        # Get keyboard state
        keys = pygame.key.get_pressed()
        dx = keys[pygame.K_d] - keys[pygame.K_a]
        dy = keys[pygame.K_s] - keys[pygame.K_w]
        if dx != 0 or dy != 0:
            logger.debug(f"Player movement: dx={dx}, dy={dy}")
        self.player.move(dx, dy)

    def check_collisions(self):
        # Check sword attacks
        if self.player.attacking:
            for enemy in self.enemies:
                if pygame.sprite.collide_circle(self.player, enemy):
                    enemy.health -= 25
                    logger.debug(f"Enemy hit by sword. Health: {enemy.health}")
                    if enemy.health <= 0:
                        enemy.kill()
                        logger.info("Enemy defeated")

        # Check enemy collisions
        for enemy in self.enemies:
            if pygame.sprite.collide_rect(self.player, enemy):
                self.player.health -= 1
                logger.debug(f"Player hit by enemy. Health: {self.player.health}")

        # Check chest collision
        if not self.chest.opened and pygame.sprite.collide_rect(self.player, self.chest):
            logger.info("Player reached the chest!")
            self.chest.open()
            self.running = False

    def update(self):
        self.all_sprites.update(self.player)
        if self.player.attack_cooldown > 0:
            self.player.attack_cooldown -= 1
        if self.player.attack_cooldown <= 0:
            self.player.attacking = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        
        # Draw health bar
        pygame.draw.rect(self.screen, RED, (10, 10, 100, 20))
        pygame.draw.rect(self.screen, GREEN, (10, 10, self.player.health, 20))
        
        pygame.display.flip()

    def run(self):
        logger.info("Starting game loop")
        while self.running:
            self.handle_events()
            self.update()
            self.check_collisions()
            self.draw()
            self.clock.tick(60)
        logger.info("Game loop ended")

if __name__ == "__main__":
    logger.info("Starting Zelda-like Dungeon game")
    game = Game()
    game.run()
    logger.info("Game ended") 