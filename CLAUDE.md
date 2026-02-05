# CLAUDE.md

## Project Overview

Mouse-Jiggle is a single-file Python utility that automatically moves and clicks the mouse at regular intervals. It prevents the computer from entering sleep/screensaver mode or triggering idle detection.

## Repository Structure

```
Mouse-Jiggle/
├── CLAUDE.md            # This file — AI assistant guidelines
├── README.md            # Project readme (placeholder)
└── MouseJiggler.py      # Main script — all application logic
```

## Tech Stack

- **Language**: Python 3
- **External dependency**: `pyautogui` (mouse/keyboard automation)
- **Standard library**: `time`, `random`

## Running the Project

```bash
# Install dependency
pip install pyautogui

# Run the script
python3 MouseJiggler.py
# Stop with Ctrl+C
```

## Code Architecture

`MouseJiggler.py` contains three functions:

- `move_mouse()` — Reads current cursor position, applies random offset (-10 to +10 px on each axis), moves cursor
- `click_mouse()` — Performs a single mouse click
- `main()` — Runs move + click in a loop every 5 seconds; handles Ctrl+C for graceful shutdown

## Development Notes

- **No build step** — this is a directly executable Python script
- **No tests, linter, or CI/CD** are configured
- **No requirements.txt** — `pyautogui` is the only external dependency
- **No .gitignore** is present

## Conventions

- Keep the project as a single-file script unless complexity demands otherwise
- Use `pyautogui` for all mouse/keyboard interactions
- Maintain Ctrl+C (`KeyboardInterrupt`) handling for clean exit
