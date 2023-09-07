notes = {}

def generate_note():
    title = input("Enter the title of the note: ")
    content = input("Enter the content of the note: ")
    notes[title] = content
    print(f"Note '{title}' has been created.")

def view_note():
    title = input("Enter the title of the note you want to view: ")
    if title in notes:
        print(f"Title: {title}")
        print(f"Content: {notes[title]}")
    else:
        print(f"Note '{title}' not found.")

while True:
    print("\nMenu:")
    print("1. Generate Note")
    print("2. View Note")
    print("4. Quit")

    choice = input("Enter your choice (1/2/4): ")
    
    if choice == '1':
        generate_note()
    elif choice == '2':
        view_note()
    elif choice == '4':
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice Please choose 1, 2, or 4.")


