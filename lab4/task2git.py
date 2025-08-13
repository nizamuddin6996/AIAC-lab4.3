def convert_cm_to_inches(cm):
    inches = cm / 2.54
    return round(inches, 3)

# Take input from console
cm_value = float(input("Enter value in centimeters: "))
result = convert_cm_to_inches(cm_value)
print(result)