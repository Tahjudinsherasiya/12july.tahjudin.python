notes = []
def generate_note():
    note = input("Enter your note: ")
    notes.append(note)
    print("Note generat successfully!")

def view_notes():
    if notes:
        print("\nYour Notes:")
        for idx, note in enumerate(notes, 1):
            print(f"{idx}. {note}")
    else:
        print("No notes.")

while True:
    print("\nMenu:")
    print("1. Generate Note")
    print("2. View Note")
    print("4. Exit")

    choice = input("Enter your choice: (1/2/4): ")

    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            generate_note()
        elif choice == 2:
            view_notes()
        elif choice == 4:
            print("Exit...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 4.")
    else:
        print("Invalid input. Please enter (1, 2, or 4).")
        
        