def format_name(full_name):
    parts = full_name.strip().split()
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    else:
        return full_name  # return as is if not exactly two parts

name = input("Enter full name (first last): ")
formatted = format_name(name)
print(f"name:{formatted}")
