class ENoteBook:
    def __init__(self):
        self.notes = []

    def generate_note(self):
        """Generate a new note."""
        note = input("Enter your note: ")
        self.notes.append(note)
        print("Note added successfully!")

    def view_notes(self):
        """View all existing notes."""
        if not self.notes:
            print("No notes found.")
        else:
            print("Your notes:")
            for i, note in enumerate(self.notes, start=1):
                print(f"{i}. {note}")

def main():
    notebook = ENoteBook()
    
    while True:
        print("\nPython E-Note Book Console Application")
        print("1. Generate Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            notebook.generate_note()
        elif choice == '2':
            notebook.view_notes()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
    