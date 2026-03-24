# AGENTS.md - AutoTex2 Development Guide

## Project Overview

AutoTex2 is a Python desktop GUI application for mathematical formula recognition (LaTeX OCR) using the TexTeller ML model via PyTorch.

- **Language**: Python (>=3.10)
- **UI Framework**: tkinter with TinUI
- **ML Framework**: PyTorch with Transformers
- **Platform**: Windows-only

## Build/Run Commands

```bash
# Install dependencies
pip install texteller tinui pystray tkwebview latex2mathml

# Run the application
python main.py

# Debug (VS Code)
# Use the "Python 调试程序: 当前文件" configuration in .vscode/launch.json
```

## Code Style Guidelines

### Naming Conventions

- **Functions**: `snake_case` (e.g., `cli_get`, `process_img`)
- **Variables**: `snake_case` (e.g., `latexstring`, `do_process`)
- **Global state**: Module-level variables in `data.py`
- **UI event handlers**: Descriptive names (e.g., `model_loaded`, `load_latex`)

### Import Style

```python
import os
os.chdir(os.path.dirname(__file__))

# Standard library
from tkinter import Tk
from concurrent.futures import ThreadPoolExecutor

# Third-party packages
from PIL import Image, ImageGrab, ImageTk
from latex2mathml.converter import convert
from tkwebview import TkWebview as Webview
from pystray import Icon, MenuItem
from tinui import *

# Local module
import data
```

### Code Patterns

- Use global state module `data.py` for shared state between modules
- Use `ThreadPoolExecutor` for background ML processing
- Bind tkinter virtual events (e.g., `<<ModelLoaded>>`, `<<ImageProcessed>>`)
- Keep UI responsive by offloading heavy work to threads

### Comments

- Keep comments concise and relevant

## Architecture

- **Event-driven**: Uses tkinter virtual events for component communication
- **Threading**: Background processing via `ThreadPoolExecutor`
- **State management**: Global module `data.py` for shared state
- **Modules**:
  - `main.py`: Main application entry and UI
  - `process.py`: Model loading and image processing
  - `data.py`: Global state module

## Dependencies

Core packages:
- `texteller` - TexTeller ML model
- `tinui` - Custom tkinter widgets
- `pystray` - System tray icon
- `tkwebview` - Web view component (Windows only)
- `latex2mathml` - LaTeX to MathML conversion
- `Pillow` - Image processing

## File Structure

```
├── main.py              # Application entry point
├── process.py           # ML model processing
├── data.py              # Global state
├── libs/                # Web resources (KaTeX)
├── asset/               # Icons and logo
├── model/               # ML model files (1.2GB, gitignored)
└── .vscode/             # VS Code debug config
```

## Notes for AI Agents

- This is a Windows-only application (uses `tkwebview`)
- The model files in `/model/` are large and gitignored
- UI labels and comments are in Chinese - maintain this convention
- No formal type hints - follow existing patterns
- No linter/formatter configured - follow existing visual style
