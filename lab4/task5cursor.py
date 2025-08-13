def read_txt_file_from_console():
    """
    Function that reads a .txt file from the console.
    Prompts the user to enter a filename and reads the file contents.
    """
    try:
        # Prompt user to enter filename
        filename = input("Enter the name of the .txt file to read: ")
        
        # Ensure filename ends with .txt extension
        if not filename.endswith('.txt'):
            filename += '.txt'
        
        # Open and read the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"\nContents of {filename}:")
            print("-" * 50)
            print(content)
            print("-" * 50)
            
            # Count and display number of lines
            lines = content.split('\n')
            line_count = len(lines)
            print(f"\nNumber of lines in the file: {line_count}")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode file '{filename}'. The file may not be a text file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    print("Text File Reader")
    print("=" * 20)
    read_txt_file_from_console()
