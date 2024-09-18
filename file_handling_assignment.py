# Python script for file handling assignment

# Task: File Creation, Writing, Reading, Appending, and Error Handling

try:
    # File Creation: Writing to the file
    with open('my_file.txt', 'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("Here is a number: 12345.\n")
        file.write("Last line for the first write.\n")
    
    # Reading the file contents and displaying them
    with open('my_file.txt', 'r') as file:
        print("Contents after writing:")
        print(file.read())
    
    # Appending to the file
    with open('my_file.txt', 'a') as file:
        file.write("Appended line 1.\n")
        file.write("Appended line 2 with a number: 6789.\n")
        file.write("Final appended line.\n")
    
    # Reading the file contents again after appending
    with open('my_file.txt', 'r') as file:
        print("Contents after appending:")
        print(file.read())

# Error Handling
except FileNotFoundError as fnf_error:
    print(f"Error: File not found - {fnf_error}")
except PermissionError as perm_error:
    print(f"Error: Permission denied - {perm_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operation completed.")
