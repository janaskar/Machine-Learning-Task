import numpy as np
import random
from sklearn.linear_model import LogisticRegression

# Define the possible moves
moves = ['R', 'P', 'S']

# Function to convert move to a number for modeling
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

# Function to play the game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("You can choose R for Rock, P for Paper, or S for Scissors. Type 'exit' to quit.")

    player_moves = []
    model = LogisticRegression(solver='saga')  # Removed multi_class parameter

    while True:
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

        # Get player's move
        player_move = input("Enter your move (R/P/S): ").upper()

        if player_move == 'EXIT':
            print("Thanks for playing!")
            break
        
        if player_move not in moves:
            print("Invalid move! Please try again.")
            continue

        player_moves.append(player_move)

        print(f"I chose: {computer_move}")

        # Determine the outcome
        result = determine_winner(player_move, computer_move)
        print(result)

# Function to determine the winner
def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "It's a tie!"
    elif (player_move == 'R' and computer_move == 'S') or \
         (player_move == 'P' and computer_move == 'R') or \
         (player_move == 'S' and computer_move == 'P'):
        return "You win!"
    else:
        return "I win!"

# Run the game
if __name__ == "__main__":
    play_game()
