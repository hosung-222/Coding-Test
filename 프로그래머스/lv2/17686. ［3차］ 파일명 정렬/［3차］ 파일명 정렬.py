import re

def solution(files):
    file_parts = [re.split('([0-9]+)', file) for file in files]
    print(file_parts)
    sorted_files = sorted(file_parts, key=lambda x: (x[0].lower(), int(x[1])))
    result = [''.join(file) for file in sorted_files]
    return result
