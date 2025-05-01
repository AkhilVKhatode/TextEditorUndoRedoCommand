# Undo/Redo Command Pattern Implementation in Python

A clean implementation of the Command design pattern to enable undo/redo functionality in text editing applications.

## Features

- Simple Command pattern implementation for undo/redo operations
- Supports basic text insertion and deletion
- Unlimited undo/redo capability (until memory permits)
- Clean separation of concerns between commands and editor
- Easy to extend with new command types

## How It Works

The system consists of three main components:

1. **Command History** - Manages the undo/redo stacks
2. **Command Objects** - Encapsulate actions and their reversal
3. **Text Editor** - Provides the interface for text manipulation

## Usage Example

```python
from text_editor import TextEditor

editor = TextEditor()

# Insert some text
editor.insert("Hello")
editor.insert(" World", 5)

# Delete text
editor.delete(5, 6)

# Undo operations
editor.undo()  # Undoes the delete
editor.undo()  # Undoes the second insert

# Redo operations
editor.redo()  # Redoes the second insert
editor.redo()  # Redoes the delete
```
