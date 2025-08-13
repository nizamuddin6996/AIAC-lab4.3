
def convert_cm_to_inches(cm):
    return round(cm / 2.54, 3)

cm = float(input("Enter length in centimeters: "))
inches = convert_cm_to_inches(cm)
print(inches)
