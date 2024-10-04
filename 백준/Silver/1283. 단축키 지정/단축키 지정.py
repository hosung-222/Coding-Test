n = int(input())

hotkeys = []
for _ in range(n):
    options = input().split()
    found = False
    result = ""

    # 각 단어의 첫 글자를 검사
    for idx, word in enumerate(options):
        if word[0].upper() not in hotkeys and not found:
            hotkeys.append(word[0].upper())
            found = True
            word = word.replace(word[0], "[" + word[0] + "]", 1)
        result += word + " "

    # 첫 글자로 단축키를 찾지 못한 경우
    if not found:
        result = ""
        for word in options:
            new_word = ""
            for char in word:
                if char.upper() not in hotkeys and not found:
                    hotkeys.append(char.upper())
                    found = True
                    new_word += "[" + char + "]"
                else:
                    new_word += char
            result += new_word + " "
    print(result.strip())
