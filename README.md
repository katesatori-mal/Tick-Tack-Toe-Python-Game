# Tick Tack Toe (Python)

A terminal-based tic-tac-toe game written in Python with no external dependencies. The board is drawn with ASCII characters and the player takes turns by entering a number from 1 to 9.

## Running it

```bash
python tick-tack-toe.py
```

No installation or dependencies required. Python 3 only.

## How to play

The board is numbered 1 through 9, left to right and top to bottom:

```
  1  |  2  |  3
  ---|-----|----
  4  |  5  |  6
  ---|-----|----
  7  |  8  |  9
```

Enter the number of the square you want. Input outside the 1–9 range is rejected and re-prompted. The board is redrawn after every move, and the game checks for a win or a draw each turn.

## How it works

| Function | Purpose |
|---|---|
| `printboard(nums)` | Renders the current board state |
| `check_draw(spaces)` | Returns `True` when all nine squares are filled |
| `check_win(spots, player, wins)` | Checks the player's marks against the winning-combination list |
| `computer_moves(spaces, wins)` | Scans winning lines for a square with two of the player's marks |

The `win` list holds every three-in-a-row combination as a tuple of board indices.

## Current status

This is a work in progress. Three things are worth knowing before you play or build on it:

**The computer never takes a turn.** `computer_moves()` is defined but never called from the game loop, and it currently only detects threatening lines without returning or placing a move. The game plays as single-player X-only until this is wired up.

**Two entries in the `win` list are wrong.** The diagonals are listed as `(0,5,8)` and `(2,5,6)`. The correct diagonals are `(0,4,8)` and `(2,4,6)` — both should pass through the center square, index 4. As written, some real wins go undetected and some non-lines register as wins.

**Occupied squares can be overwritten.** There's no check for whether a square is already taken, so entering the same number twice silently replaces the previous mark.

## Roadmap

- [ ] Fix the two diagonal entries in the `win` list
- [ ] Reject moves onto already-occupied squares
- [ ] Finish `computer_moves()` so it returns an index and place the O
- [ ] Add blocking logic: take the winning square if available, otherwise block the player's two-in-a-row
- [ ] Add a play-again prompt at the end of a game
