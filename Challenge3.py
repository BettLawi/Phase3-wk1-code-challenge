def alphabet_characters(string):
    consonants = "bcdfghjklmnpqrstvwxyz"
    max_value = 0
    current_value = 0

    for character in string:
        if character in consonants:
            current_value += ord(character) - ord('a')+1
            max_value = max(max_value, current_value)
        else:
            current_value = 0

    return max_value            
    
print(alphabet_characters("zodiacs"))  # Output: 26
print(alphabet_characters("strength"))  # Output: 57
