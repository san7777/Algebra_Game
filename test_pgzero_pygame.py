"""
cd /Users/sandra/Library/CloudStorage/Dropbox/GooseApp/Algebra_Game/space_gems
deactivate 
source env/bin/activate
pwd
clear;python3 test_pgzero_pygame.py
"""
import pygame
import pgzrun

# Initialize Pygame mixer for audio
pygame.mixer.init()

# Load a sound
sound = pygame.mixer.Sound('./sounds/background_music.mp3')
sound.play()

# Pygame Zero game setup
WIDTH = 400
HEIGHT = 300

# A simple actor to display
actor = Actor('hero_level1', (WIDTH // 2, HEIGHT // 2))

def draw():
	screen.clear()
	actor.draw()

def update():
	pass



# Start the game loop
pgzrun.go()
