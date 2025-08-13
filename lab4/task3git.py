def format_name():
    name = input("Enter full name (First Last): ").strip()
    parts = name.split()
    if len(parts) == 2:
        formatted = f"{parts[1]} {parts[0]}"
        print(f"name:{formatted}")
    else:
        print("Please enter a name in 'First Last' format.")

if __name__ == "__main__":
    format_name()