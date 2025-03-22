# Zelda-like Dungeon Game

A simple 2D dungeon game inspired by The Legend of Zelda, built with Pygame.

## Features

- Player character with movement and sword attack
- Enemy AI that chases the player
- Health system
- Treasure chest goal
- Sprite-based graphics
- Logging system for debugging

## Controls

- WASD: Move the player
- Spacebar: Attack with sword

## Requirements

- Python 3.x
- Pygame 2.5.2

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ealemank/cursor-hello-world.git
cd cursor-hello-world
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Game

```bash
python zelda_game.py
```

## Project Structure

- `zelda_game.py`: Main game file
- `create_sprites.py`: Script to generate game sprites
- `assets/`: Directory containing game sprites
- `requirements.txt`: Project dependencies
- `game.log`: Game logging file (generated during runtime)

## Development

The game uses Python's logging system for debugging. Logs are written to both the console and `game.log` file.

## License

This project is open source and available under the MIT License. 