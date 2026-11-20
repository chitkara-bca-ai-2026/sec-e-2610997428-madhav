print("Input: Python 3.14 is amazing for AI!")

sentence = input("\nEnter a sentence: ")

words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0

for char in sentence:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    else:
        special_characters += 1

total_characters = len(sentence)
total_letters = vowels + consonants

if total_letters > 0:
    vowel_percentage = (vowels / total_letters) * 100
else:
    vowel_percentage = 0

print("\n==========================================")
print("DOCUMENT ANALYSIS REPORT")
print("==========================================")
print("Sentence:", sentence)
print("Total characters:", total_characters)

print("\n--- Character Breakdown ---")
print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special_characters)

print("\n--- Summary ---")
print("Total letters:", total_letters)
print(f"Vowel percentage: {vowel_percentage:.1f}%")

print("\n==========================================")
print("Analysis Complete!")
print("==========================================")
