# Tic-Tac-Toe

A console-based implementation of Tic-Tac-Toe developed in Python. This application features a single-player mode against a computer opponent with variable difficulty settings.

## Features

- **Player vs Computer**: Play against an automated opponent.
- **Difficulty Levels**:
  - **Easy**: The computer makes random moves.
  - **Normal**: The computer attempts to win but may miss blocking opportunities.
  - **Hard**: The computer plays strategically but makes occasional errors.
  - **Hell**: The computer plays optimally using the Minimax algorithm.
- **Clean Interface**: A straightforward command-line interface.

## Prerequisites

- Python 3.8 or higher.

## Installation

This project relies on the standard Python library and does not require external dependencies.

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Usage

Upon collecting the source code, run the main script to start the game. You will be prompted to:
1. Enter your username.
2. Select a difficulty level (1-4).
3. Enter board positions (0-8) to place your marker.

## Development

The codebase uses a modular architecture separating the game engine, board logic, and AI.

### Running Tests

To verify the integrity of the game logic and AI algorithms, run the unit test suite with the following command:

```bash
python -m unittest discover tests -v
```

## License

This project is licensed under the MIT License.