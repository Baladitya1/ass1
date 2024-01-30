def vowel_string(input_text):
    vowels_set = set("aeiouAEIOU")
    c_count = 0
    v_count = 0

#For counting the number of vowels and consonants
    for char in input_text:
        if char.isalpha():
            if char in vowels_set:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

# Gathering the  input
user_text = input("Please enter a text: ")

# Final result by calling the funtion "vowel string" , v=vowels , c=consonants
v, c= vowel_string(user_text)
print(f"Number of vowels: {v}")
print(f"Number of consonants: {c}")
