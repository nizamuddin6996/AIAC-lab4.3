def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

string = input("Enter a string: ")
num_vowels = count_vowels(string)
print(f"{num_vowels} vowels")
