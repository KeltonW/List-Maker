import os

def selectDirectory():
    directory = input("Please enter a directory to work in: ")
    # Set directory for the new file
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist! Do you want to create it?\nY/n ")
        answer = input()
        if answer.lower() == 'y':
            os.makedirs(directory)
            print(f"Directory '{directory}' created successfully.")
        else:
            print("Exiting without creating the directory.")
            return
    else:
        os.chdir(directory)
        print(f"Moved to '{directory}'.")
        
# Create new file in the current working directory if it does not exist
def newlist(filename):
    selectDirectory()
    
    # Check if file already exists. If not, cancel the operation
    if os.path.exists(f"{filename}.txt"):
        print(f"{filename}.txt already exists!")
        return
    else:
        newfile = open(f"{filename}.txt", 'w')
        newfile.close()

# Append to existing file
def appendtolist(filename, item):
    selectDirectory()

    if not os.path.exists(f"{filename}.txt"):
        print(f"{filename}.txt does not exist!")
        return
    else:
        openfile = open(f"{filename}.txt", 'a')
        openfile.write(f"{item}\n")
        openfile.close()

# Print all text in existing file
def readfile(filename):
    selectDirectory()

    if not os.path.exists(f"{filename}.txt"):
        print(f"{filename}.txt not found!")
    else:
        for line in open(f"{filename}.txt", 'r'):
            print(line.strip())

# Delete existing file
def deletefile(filename):
    selectDirectory()

    if not os.path.exists(f"{filename}.txt"):
        print(f"{filename}.txt not found!")
    else:
        os.remove(f"{filename}.txt")
        print(f"{filename}.txt deleted successfully.")

# Main loop
while True:
    print("Welcome! Please select an option:\n")
    print("0. Quit")
    print("1. Create a new list")
    print("2. Add to an existing list")
    print("3. Read a list")
    print("4. Delete a list")
    choice = input()

    match choice:
        case "0":
            print("Goodbye!")
            break
        case "1":
            filename = input("Enter name for the new list (Exclude format): ")
            newlist(filename)
            print(f"{filename}.txt created successfully.")
        case "2":
            filename = input("Enter the name of the list to append to (Exclude format): ")
            item = input("Enter text to add: ")
            appendtolist(filename, item)
            print(f"Item '{item}' appended to {filename}.txt successfully.")
        case "3":
            filename = input("Enter the name of the list to read (Exclude format): ")
            print(f"Reading {filename}.txt...")
            readfile(filename)
            print("End of list.")
        case "4":
            filename = input("Enter the name of the list to delete (Exclude format): ")
            print(f"Deleting {filename}.txt...")
            deletefile(filename)
        case _:
            print("Invalid option. Please try again.")
            continue
    print("\n")