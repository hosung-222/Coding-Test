n = int(input())
words = []
hotkey = []
for _ in range(n):
    find = False
    temp = list(input().split())
    new_word = ""
    for c in temp:
        if c[0].upper() not in hotkey and not find:
            new_word += "[" + c[0] +"]" +c[1:] + " "
            hotkey.append(c[0].upper())
            find = True
        else:
            new_word += c + " "
    if find:
        words.append(new_word)

    if not find:
        new_word = ""
        for s in temp:
            for c in s:
                if c.upper() not in hotkey and not find:
                    new_word += "[" + c + "]"
                    hotkey.append(c.upper())
                    find = True
                else:
                    new_word += c
            new_word += " "
        words.append(new_word)

for w in words:
    print(w)