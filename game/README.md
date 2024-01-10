
---

# Rock, Paper, Scissors Game

This Python program is an implementation of the classic game Rock, Paper, Scissors, integrated with cartesi rollup.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Game Logic](#game-logic)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This program demonstrates a basic implementation of the Rock, Paper, Scissors game using Python. It interacts with an cartesi rollup to handle game states, using the given rollup mechanism.

## Features

- Allows a player to make a move in the game.
- Simulates the computer's move randomly.
- Determines the game result (win, lose, or draw).
- Communicates game results with an cartesi rollup.

## Requirements

- Install the required dependencies:

   ```bash
   npm install -g @sunodo/cli
   ```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/LamsyA/cartesi-masterclass.git
   ```

   ```bash
   cd game
   ```



## Usage

1. build a Cartesi machine and run a local node for the application:

   ```bash
   sunodo build
   sunodo run
   ```

2. Sending inputs:
     ```bash
   sunodo send generic
   ```

   

## Game Logic

The game follows these basic rules:

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

The player makes a move, which is then compared to the computer's randomly generated move. The program determines the game result based on these moves.

## Contributing

Contributions are welcome! If you want to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

