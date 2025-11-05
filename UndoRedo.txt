undo_stack = []
redo_stack = []
document = ""

def make_change(text):
    global document, undo_stack, redo_stack
    undo_stack.append(document) 
    document += text           
    redo_stack.clear()         

def undo_action():
    global document, undo_stack, redo_stack
    if undo_stack:
        redo_stack.append(document)    
        document = undo_stack.pop()    
    else:
        print("Nothing to undo.")

def redo_action():
    global document, undo_stack, redo_stack
    if redo_stack:
        undo_stack.append(document)    
        document = redo_stack.pop()    
    else:
        print("Nothing to redo.")

def display_document_state():
    print("Current Document State:\n", document)


while True:
    print("\nChoose operation: 1) Make Change 2) Undo 3) Redo 4) Display 5) Exit")
    choice = input("Enter choice number: ").strip()
    if choice == '1':
        change = input("Enter text to add: ")
        make_change(change)
        display_document_state()
    elif choice == '2':
        undo_action()
        display_document_state()
    elif choice == '3':
        redo_action()
        display_document_state()
    elif choice == '4':
        display_document_state()
    elif choice == '5':
        print("Exiting.")
        break
    else:
        print("Invalid choice. Try again.")