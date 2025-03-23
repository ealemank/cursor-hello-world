import pygame
import numpy as np
import os

# Initialize Pygame mixer
pygame.mixer.init(44100, -16, 1, 512)

# Create sounds directory if it doesn't exist
if not os.path.exists('assets/sounds'):
    os.makedirs('assets/sounds')

def create_sword_sound():
    # Create a "whoosh" sound for sword swing
    sample_rate = 44100
    duration = 0.1  # seconds
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Create a frequency sweep from high to low
    freq_start = 1000
    freq_end = 200
    freq = np.linspace(freq_start, freq_end, len(t))
    
    # Generate the sound wave
    wave = np.sin(2 * np.pi * freq * t)
    
    # Apply envelope
    envelope = np.exp(-5 * t)
    wave = wave * envelope
    
    # Convert to 16-bit integer
    wave = np.int16(wave * 32767)
    
    # Create sound buffer
    sound = pygame.sndarray.make_sound(wave)
    return sound

def create_hit_sound():
    # Create a "thud" sound for enemy hit
    sample_rate = 44100
    duration = 0.1  # seconds
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Create a low frequency thud
    freq = 100
    wave = np.sin(2 * np.pi * freq * t)
    
    # Apply envelope
    envelope = np.exp(-10 * t)
    wave = wave * envelope
    
    # Convert to 16-bit integer
    wave = np.int16(wave * 32767)
    
    # Create sound buffer
    sound = pygame.sndarray.make_sound(wave)
    return sound

# Generate and save sound effects
sword_sound = create_sword_sound()
hit_sound = create_hit_sound()

# Save the sounds
pygame.sndarray.save(sword_sound, 'assets/sounds/sword_swing.mp3')
pygame.sndarray.save(hit_sound, 'assets/sounds/enemy_hit.mp3')

print("Sound effects created successfully!") 