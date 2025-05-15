import pygetwindow as gw

# Get a list of all open windows
windows = gw.getAllWindows()

# Print the list of windows
for i, window in enumerate(windows):
    print(f"{i+1}. {window.title}")

# Ask the user to select a window
while True:
    try:
        choice = int(
            input("Enter the number of the window you want to select: "))
        if 1 <= choice <= len(windows):
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Get the selected window
selected_window = windows[choice - 1]

# Print the title of the selected window
print(f"You selected: {selected_window.title}")

# Now you can use the selected window
