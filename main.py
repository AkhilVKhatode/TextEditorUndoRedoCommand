class Command:
    def execute(self):
        pass
    def undo(self):
        pass

class CommandHistory:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
    
    def execute(self, command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()
    
    def undo(self):
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)
    
    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.undo_stack.append(command)

class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = CommandHistory()
    
    def insert(self, text, position=None):
        position = position if position is not None else len(self.text)
        self.history.execute(InsertCommand(self, text, position))
    
    def delete(self, position, length):
        self.history.execute(DeleteCommand(self, position, length))
    
    def undo(self):
        self.history.undo()
    
    def redo(self):
        self.history.redo()

class InsertCommand(Command):
    def __init__(self, editor, text, position):
        self.editor = editor
        self.text = text
        self.position = position
    
    def execute(self):
        self.editor.text = (self.editor.text[:self.position] + 
                           self.text + 
                           self.editor.text[self.position:])
    
    def undo(self):
        self.editor.text = (self.editor.text[:self.position] + 
                           self.editor.text[self.position + len(self.text):])

class DeleteCommand(Command):
    def __init__(self, editor, position, length):
        self.editor = editor
        self.position = position
        self.length = length
        self.deleted = ""
    
    def execute(self):
        self.deleted = self.editor.text[self.position:self.position+self.length]
        self.editor.text = (self.editor.text[:self.position] + 
                           self.editor.text[self.position+self.length:])
    
    def undo(self):
        self.editor.text = (self.editor.text[:self.position] + 
                           self.deleted + 
                           self.editor.text[self.position:])

# Example usage
editor = TextEditor()
print("Start:", editor.text)

editor.insert("Hello")
print("After insert 'Hello':", editor.text)

editor.insert(" World", 5)
print("After insert ' World' at pos 5:", editor.text)

editor.delete(5, 6)
print("After delete 6 chars at pos 5:", editor.text)

print("\n--- Undo ---")
editor.undo()
print("Undo 1:", editor.text)

editor.undo()
print("Undo 2:", editor.text)

print("\n--- Redo ---")
editor.redo()
print("Redo 1:", editor.text)

editor.redo()
print("Redo 2:", editor.text)
