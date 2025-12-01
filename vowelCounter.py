text = input("Enter a string: ")
vowels = "aeiou"
vowel_count = 0

for char in text:
    if char.lower() in vowels:
        vowel_count += 1
        
print(f"Charaters:{len(text)}")
print (f"Vowels:{vowel_count}")