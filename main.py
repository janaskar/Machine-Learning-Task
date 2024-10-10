#!/usr/bin/env python3

import pygame
import random
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np
from sklearn.linear_model import LogisticRegression
from PIL import Image

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors with Stats")

# Fonts and colors
font = pygame.font.Font(None, 36)
WHITE = "#FFFFFF"
BLACK = "#000000"
GREEN = "#4CAF50"
YELLOW = "#FFC107"
RED = "#FF6347"

# Game variables
moves = ['R', 'P', 'S']
player_move = None
computer_move = None
result = None

# Stats
wins = 0
ties = 0
losses = 0
player_moves = []

model = LogisticRegression(solver='saga')  # Removed multi_class parameter

# Functions
def move_to_number(move):
    return moves.index(move)

# Function to counter the player's predicted move
def counter_move(predicted_move):
    if predicted_move == 'R':
        return 'P'
    elif predicted_move == 'P':
        return 'S'
    elif predicted_move == 'S':
        return 'R'

def get_winner(player, computer):
    global wins, losses, ties
    if player == computer:
        ties += 1
        return "It's a tie!"
    elif (player == 'R' and computer == 'S') or \
         (player == 'P' and computer == 'R') or \
         (player == 'S' and computer == 'P'):
        wins += 1
        return "You win!"
    else:
        losses += 1
        return "Computer wins!"

def display_text(text, x, y, color=WHITE):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def generate_pie_chart():
    # Check if there is any data to display
    total_games = wins + ties + losses
    if total_games == 0:
        return None  # Return None if there is no data yet

    # Create a pie chart using matplotlib
    sizes = [wins, ties, losses]
    colors = [GREEN, YELLOW, RED]
    plt.figure(figsize=(2, 2))  # Size of the pie chart
    plt.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio to ensure the pie is circular
    
    # Save the pie chart to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='PNG', facecolor='black')  # Save the image with black background
    buf.seek(0)
    
    return buf

def display_pie_chart():
    pie_chart_img = generate_pie_chart()
    if pie_chart_img is None:
        display_text("No data yet.", WIDTH - 200, 100)  # Display message if no data
    else:
        # Generate the pie chart and convert it to a Pygame surface
        img = Image.open(pie_chart_img)
        img = img.resize((150, 150))  # Resize the image
        img = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
        
        # Display the pie chart on the screen
        screen.blit(img, (WIDTH - 300, 300))

def main():
    global player_move, computer_move, result

    # Main loop
    running = True
    while running:
        screen.fill(BLACK)
        display_text("Press R for Rock, P for Paper, S for Scissors", 50, 50)
        
        # Move prediction and game logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player_move = 'R'
                elif event.key == pygame.K_p:
                    player_move = 'P'
                elif event.key == pygame.K_s:
                    player_move = 'S'
                
                # Computer's move and game result
                if player_move:
                    # Predict the next move based on history
                    if len(player_moves) > 1:
                        X = np.array([move_to_number(move) for move in player_moves[:-1]]).reshape(-1, 1)
                        y = np.array([move_to_number(move) for move in player_moves[1:]])
                        
                        # Check if there are at least two different classes
                        if len(set(y)) > 1:  # Only fit the model if we have more than one class
                            model.fit(X, y)
                            prediction = model.predict(np.array([[move_to_number(player_moves[-1])]]))[0]
                            predicted_move = moves[prediction]
                            print(f"I predict your next move will be: {predicted_move}")
                            # Determine the computer's counter move
                            computer_move = counter_move(predicted_move)
                        else:
                            print("Not enough variety in your moves to make a prediction.")
                            computer_move = random.choice(moves)  # Fallback to random move
                    else:
                        predicted_move = None
                        computer_move = random.choice(moves)  # Randomly select the computer's move

                    result = get_winner(player_move, computer_move)
                    player_moves.append(player_move)

        # Display choices and result
        if player_move:
            display_text(f"Player chose: {player_move}", 50, 150)
            display_text(f"Computer chose: {computer_move}", 50, 200)
            display_text(result, 50, 250)

            # Display wins, losses, and ties with the same colors as the pie chart
            display_text(f"Wins: {wins}", 200, 300, GREEN)
            display_text(f"Losses: {losses}", 200, 350, RED)
            display_text(f"Ties: {ties}", 200, 400, YELLOW)

            # Display pie chart
            display_pie_chart()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
