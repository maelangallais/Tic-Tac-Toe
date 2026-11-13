# ⭕ Tic-Tac-Toe Collection (NumWorks)

A comprehensive collection of **Tic-Tac-Toe** games and strategic variants designed for the **NumWorks** calculator in MicroPython.

Rather than just one single game, this repository explores the progression of Tic-Tac-Toe from early prototypes to deep, highly tactical variants (Ultimate Tic-Tac-Toe, FIFO Vanishing Tic-Tac-Toe, and Gobblet Gobblers-style sized pieces).

---

## 🎮 The Variants

```
Tic-Tac-Toe/
├── 1_classic_turtle/        # Classic Tic-Tac-Toe (Turtle graphics)
├── 2_classic_interface/     # Classic Tic-Tac-Toe with UI & selection grid
├── 3_ultimate_tictactoe/    # Strategic nested 9x9 Ultimate Tic-Tac-Toe
├── 4_vanishing_tictactoe/   # Memory / FIFO Tic-Tac-Toe (max 3 pieces per player)
└── 5_gobblet_sized_pieces/  # Stacking Tic-Tac-Toe with 9 tiered piece sizes
```

---

### 1. Classic Turtle (`1_classic_turtle/`)
- **Script** : `tictactoe_classic.py`
- **Creation date** : April 03, 2023
- **Description** : The original proof-of-concept implementation rendered entirely using the calculator's `turtle` module. A straightforward 2-player local game.

---

### 2. Classic with Interface (`2_classic_interface/`)
- **Script** : `tictactoe_interface.py`
- **Creation date** : April 10, 2023
- **Description** : An improved iteration of the classic game featuring a dedicated user interface, active cursor highlighting, and rewritten win-detection logic.

---

### 3. Ultimate Tic-Tac-Toe (`3_ultimate_tictactoe/`)
- **Script** : `ultimate_tictactoe.py`
- **Creation date** : October 08, 2023
- **Rules & Gameplay** :
  - A nested 3×3 grid of 9 local Tic-Tac-Toe boards.
  - To claim a macro-cell on the main board, you must win the mini-game inside it.
  - **Board Routing** : The cell you pick in a local board dictates which sub-grid the next player must play in (e.g. playing in the top-right cell sends your opponent to the top-right mini-board).
  - If the target sub-grid is already resolved or occupied, a fallback traversal routes play to the next available sub-grid.
  - If a mini-board ends in a draw, ownership is determined by majority piece dominance.
  - **Strategy** : Far deeper than standard Tic-Tac-Toe, virtually eliminating forced draws.

---

### 4. Vanishing Tic-Tac-Toe (`4_vanishing_tictactoe/`)
- **Script** : `vanishing_tictactoe.py`
- **Creation date** : April 15, 2024
- **Rules & Gameplay** :
  - Each player can only maintain **3 pieces** simultaneously on the grid.
  - Placing a 4th piece causes your oldest piece to vanish (First-In, First-Out queue).
  - **Strategy** : Demands continuous forward planning and memory tracking, preventing stalemates and creating dynamic, fast-paced matches.

---

### 5. Gobblet / Tiered-Size Tic-Tac-Toe (`5_gobblet_sized_pieces/`)
- **Script** : `gobblet_tictactoe.py`
- **Creation date** : July 02, 2024
- **Rules & Gameplay** :
  - Each player receives an arsenal of **9 pieces with tiered sizes** (ranked 1 to 9).
  - **Covering Mechanic** : Larger pieces can be played directly on top of smaller pieces already on the board (whether belonging to the opponent or yourself). A size 6 piece can only be covered by sizes 7, 8, or 9.
  - **Selection UI** : Select a target cell, then choose which available piece size from your inventory to drop. Press `Clear` to cancel selection.
  - **End Conditions** : Win by aligning 3 visible pieces of your color. Stalemate/loss can occur if a player whose turn it is has no piece large enough to make a legal move.

---

## ⌨️ General Controls

All variants follow intuitive, standardized calculator controls:
- **Directional Arrows** : Move the active selection cursor across cells or sub-grids.
- **OK / EXE** : Place a piece / confirm choice.
- **Clear** *(in Gobblet mode)* : Cancel piece selection and return to cell targeting.

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators.
- Uses `kandinsky`, `ion`, and `turtle` (for classic variants).
- Tested on NumWorks (N0110 / N0120) and compatible online emulators.
