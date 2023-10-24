import os

def create_file(filename):
    with open(filename, 'w') as file:
        pass

def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")

def edit_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Current content of {filename}:")
            print(content)
            new_content = input("Enter the new content:\n")
            with open(filename, 'w') as file:
                file.write(new_content)
    except FileNotFoundError:
        print("File not found.")

def main():
    print("Simple Text Editor")
    
    while True:
        print("\nMenu:")
        print("1. Create a new file")
        print("2. Open an existing file")
        print("3. Edit a file")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            filename = input("Enter the new file name: ")
            create_file(filename)
        elif choice == "2":
            filename = input("Enter the file name to open: ")
            open_file(filename)
        elif choice == "3":
            filename = input("Enter the file name to edit: ")
            edit_file(filename)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()