char_map = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

illegal_chars = []

with open("input.txt") as f:
    for line in f:
        left = ""
        right = ""
        for char in line.rstrip():
            if char == '(' or char == '[' or char == '{' or char == '<':
                left += char
            else:
                right += char
                if char != char_map[left[-1]]:
                    illegal_chars.append(char)
                    break
                else:
                    left = left[:-1]

error_score = 0
for char in illegal_chars:
    if char == ')':
        error_score += 3
    elif char == ']':
        error_score += 57
    elif char == '}':
        error_score += 1197
    elif char == '>':
        error_score += 25137

print(error_score)
