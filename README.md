# 🎮 Six Shapes Game

A console-based implementation of the **Six Shapes** board game developed in **Python** as the final project for the **Fundamentals of Programming** course at K. N. Toosi University of Technology (KNTU).

---

## 📖 Project Overview

Six Shapes is a two-player strategic board game played on a **5×5 grid**.

Each player controls **three ships**, and the objective is to move all of your ships to the opposite side of the board before your opponent does.

This project implements the core mechanics of the game using Python and runs entirely in the terminal.

---

## 🎯 Features

- ✅ Two-player gameplay
- ✅ 5×5 board representation
- ✅ Turn-based movement system
- ✅ Input validation
- ✅ ASCII board visualization
- ✅ Simple and modular code structure
- ✅ Console-based interface

---

## 🕹️ Game Rules

### Initial Setup

- The game is played on a **5×5 board**.
- Each player starts with **3 ships**.
- Player 1 begins from one side of the board.
- Player 2 begins from the adjacent side.

---

### Movement

During each turn:

- A player selects one of their ships.
- The selected ship moves **one square forward**.
- If an opponent's ship is directly in front, the player may **jump over it**.
- Jumping is only allowed if the landing square is empty.
- If no legal move exists for a selected ship, another ship must be chosen.

---

### Free Turn

If a player has **no valid legal moves**, their turn is skipped and the opponent immediately receives another turn.

---

### Winning Condition

The first player who successfully moves **all three ships** to the opposite side of the board wins the game.

---

## 📂 Project Structure

```
SixShapes/
│
├── SixShapes__Game.py     # Main game source code
├── README.md              # Project documentation
└── Project Specification.pdf
```

---

## 🚀 Getting Started

### Requirements

- Python 3.8 or newer

No external libraries are required.

---

### Run the Game

Clone the repository:

```bash
git clone https://github.com/your-username/SixShapes.git
```

Navigate into the project:

```bash
cd SixShapes
```

Run the game:

```bash
python SixShapes__Game.py
```

---

## 💻 Example Gameplay

```
+-----+-----+-----+-----+-----+
|     | P1  |     |     |     |
+-----+-----+-----+-----+-----+
|     | P1  |     |     |     |
+-----+-----+-----+-----+-----+
|     | P1  |     |     |     |
+-----+-----+-----+-----+-----+

Player 1, enter ship number (1-3):
```

---

## 🛠 Technologies Used

- Python 3
- Console (CLI)
- Standard Python Library

---

## 📚 Course Information

**Course:**
Fundamentals of Programming

**University:**
K. N. Toosi University of Technology (KNTU)

**Semester:**
Fall 2023

---

## 🔍 Future Improvements

Possible enhancements include:

- Graphical User Interface (Tkinter or Pygame)
- Full implementation of jump mechanics
- Automatic detection of blocked players
- Smarter move validation
- AI opponent
- Multiplayer over network
- Move history
- Save and load game
- Unit tests
- Better object-oriented architecture

---

## 🤝 Contributing

Contributions, improvements, and bug reports are welcome.

Feel free to fork the repository and submit a Pull Request.

---

## 📄 License

This project was created for educational purposes as a  KNTU university programming assignment.

You are free to study and modify the source code for learning purposes.

---

## 👨‍💻 Arpourbasir

**Alireza Pourbasir**

GitHub:
https://github.com/Arpourbasir

---

⭐ If you found this project useful, consider giving it a star!
