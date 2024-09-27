vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    password = input()
    if password == 'end':
        break
    
    total_vowel = 0
    vowel_count = 0
    consonant_count = 0
    acceptable = True

    for word in password:
        if word in vowel:
            vowel_count += 1
            consonant_count = 0
            total_vowel += 1
        else:
            consonant_count += 1
            vowel_count = 0
        
        if consonant_count == 3 or vowel_count == 3:
            acceptable = False
            break
    
    if total_vowel == 0:
        acceptable = False

    for index in range(1, len(password)):
        if password[index] == password[index - 1] and password[index] not in ['e', 'o']:
            acceptable = False
            break

    if acceptable:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")