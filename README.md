# Rock Paper Scissors with Stats and Machine Learning

This is a fun **Rock Paper Scissors** game built with **Pygame** that includes stats tracking and a simple machine learning model to predict the player's next move. The game offers interactive gameplay where the computer tries to predict and counter the player's choices, and visualizes the results with a pie chart showing the player's win/loss/tie statistics.

## Requirements

Before running the game, you'll need Python 3.x installed. The dependencies are listed in the `requirements.txt` file, which can be installed within a virtual environment.

### Setting up a Virtual Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/janaskar/Machine-Learning-Task.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Machine-Learning-Task
   ```

3. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment**:

   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### How to Play

Once the environment is set up and dependencies are installed, you can start the game:

1. Run the game:
   ```bash
   python3 game.py
   ```

2. The game will open a window where you can play by pressing:
   - `R` for Rock
   - `P` for Paper
   - `S` for Scissors

   The computer will then predict your next move and try to counter it!

3. A pie chart showing your win/loss/tie statistics will update in real-time as you play.

## Future Enhancements

- Adding icons for Rock, Paper, and Scissors instead of plain text.
- Introducing more advanced machine learning models for better predictions.