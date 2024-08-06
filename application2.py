"""
cd /Users/sandra/Library/CloudStorage/Dropbox/GooseApp/Algebra_Game/
deactivate 
source env/bin/activate
pwd
clear;python3 main.py
"""
import pygame
import random
import time
import os
from flask import Flask

app = Flask(__name__)

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algebra Adventure")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NAVY_BLUE = (0, 0, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Algebra equations
equations = [
    {"question": "2x + 3 = 7", "answer": "2"},
    {"question": "3x - 4 = 5", "answer": "3"},
    {"question": "x / 2 + 5 = 7", "answer": "4"},
    {"question": "5x + 2 = 17", "answer": "3"},
    {"question": "4x - 2 = 10", "answer": "3"},
    {"question": "6x / 2 = 9", "answer": "3"},
    {"question": "x + 4 = 9", "answer": "5"},
    {"question": "10x - 5 = 25", "answer": "3"},
    {"question": "2x + 7 = 11", "answer": "2"},
    {"question": "3x - 2 = 7", "answer": "3"},
    {"question": "7x + 3 = 24", "answer": "3"},
    {"question": "9x / 3 = 9", "answer": "3"},
    {"question": "5x + 15 = 30", "answer": "3"},
    {"question": "8x - 4 = 28", "answer": "4"},
    {"question": "6x + 6 = 24", "answer": "3"},
    {"question": "5x - 2 = 8", "answer": "2"},
    {"question": "x + 9 = 8", "answer": "-1"},
    {"question": "9x - 2 = 16", "answer": "2"},


]

# Load superhero images and scale them down
superhero_images = [
    pygame.transform.scale(pygame.image.load(f'./images/hero_level{i}.png'), (200, 200)) for i in range(1, 11)
]


# Load background image as a small logo
background_logo = pygame.image.load('./images/background_logo.png').convert()
background_logo = pygame.transform.scale(background_logo, (200, 200))

# Load sounds
correct_sound = pygame.mixer.Sound('./sounds/correct.mp3')
wrong_sound = pygame.mixer.Sound('./sounds/wrong.mp3')
level_up_sound = pygame.mixer.Sound('./sounds/level_up.wav')

# Background music
pygame.mixer.music.load('./sounds/background_music.mp3')
pygame.mixer.music.play(-1)  # Loop the background music

# Game variables
def reset_game():
    global current_equation, input_text, score, start_time, timer, running, show_notification, restart_button_rect, correct_streak, show_level_up, level_up_time, high_score
    current_equation = random.choice(equations)
    input_text = ''
    score = 0
    start_time = time.time()
    timer = 30  # 30 seconds for each question
    running = True
    show_notification = False
    restart_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
    correct_streak = 0
    show_level_up = False
    level_up_time = 0
    high_score = load_high_score()

def load_high_score():
    if os.path.exists('high_score.txt'):
        with open('high_score.txt', 'r') as file:
            return int(file.read())
    else:
        return 0

def save_high_score(score):
    with open('high_score.txt', 'w') as file:
        file.write(str(score))

reset_game()

# Main game loop
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if running:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text == current_equation["answer"]:
                        score += 10
                        correct_streak += 1
                        
                        if correct_streak == 3:
                            show_level_up = True
                            level_up_sound.play()
                            level_up_time = time.time()
                            correct_streak = 0  # Reset the streak
                        else:
                            correct_sound.play()
                        
                        if score > high_score:
                            high_score = score
                            save_high_score(high_score)
                        
                        if score >= 100:
                            running = False
                            show_notification = True
                        
                        current_equation = random.choice(equations)
                        input_text = ''
                        start_time = time.time()  # Reset the timer
                    else:
                        score = 0
                        correct_streak = 0  # Reset the streak
                        wrong_sound.play()
                        input_text = ''
                        start_time = time.time()  # Reset the timer
                else:
                    input_text += event.unicode
        elif show_notification:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if restart_button_rect.collidepoint(event.pos):
                    reset_game()

    # Check if timer has run out
    if running and elapsed_time > timer:
        score = 0
        correct_streak = 0  # Reset the streak
        current_equation = random.choice(equations)
        input_text = ''
        start_time = time.time()  # Reset the timer

    # Clear screen
    screen.fill(WHITE)

    if running:
        # Display equation with background
        question_text = font.render(current_equation["question"], True, BLACK)
        question_rect = question_text.get_rect(center=(WIDTH // 2, 150))
        background_rect = pygame.Rect(question_rect.left - 10, question_rect.top - 10, question_rect.width + 20, question_rect.height + 20)
        pygame.draw.rect(screen, WHITE, background_rect)
        screen.blit(question_text, question_rect)
        
        # Display input box
        input_box = pygame.Rect(300, 300, 140, 50)
        pygame.draw.rect(screen, BLACK, input_box, 2)
        
        # Render the current input text
        text_surface = font.render(input_text, True, BLACK)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        
        # Display score
        score_text = small_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        
        # Display timer
        timer_text = small_font.render(f"Time left: {int(timer - elapsed_time)}", True, BLACK)
        screen.blit(timer_text, (WIDTH - 200, 10))

        # Display completion bar
        pygame.draw.rect(screen, BLACK, [10, 50, 200, 30], 2)  # Outline of the bar
        pygame.draw.rect(screen, GREEN, [12, 52, score * 2, 26])  # Fill the bar

        # Display the small logo in the bottom left corner
        screen.blit(background_logo, (10, HEIGHT - 210))

        # Display superhero
        hero_index = min(score // 10, len(superhero_images) - 1)
        hero_image = superhero_images[hero_index]
        hero_rect = hero_image.get_rect(center=(WIDTH - 125, HEIGHT // 2))  # Moved left by 50 pixels
        screen.blit(hero_image, hero_rect)
        
        # Display level up notification
        if show_level_up and time.time() - level_up_time < 2:  # Show level up for 2 seconds
            level_up_text = font.render("LEVEL UP!!!", True, BLACK)
            level_up_rect = level_up_text.get_rect(center=(WIDTH // 2, HEIGHT - 50))
            screen.blit(level_up_text, level_up_rect)
        else:
            show_level_up = False

    elif show_notification:
        # Display "You're a Brainy Banana!" notification
        screen.fill(WHITE)
        notification_text = font.render("You're a Brainy Banana!", True, NAVY_BLUE)
        notification_rect = notification_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(notification_text, notification_rect)

        # Display high score
        high_score_text = small_font.render(f"High Score: {high_score}", True, BLACK)

        screen.blit(high_score_text, (WIDTH // 2 - 50, HEIGHT // 2 - 50))

        # Draw the restart button
        pygame.draw.rect(screen, NAVY_BLUE, restart_button_rect)
        restart_text = small_font.render("Restart", True, WHITE)
        restart_text_rect = restart_text.get_rect(center=restart_button_rect.center)
        screen.blit(restart_text, restart_text_rect)
    
    pygame.display.flip()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))

