char_map = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

completion_strings = []


def build_completion_string(left_string):
    completion_string = ""
    for i in range(len(left_string) - 1, -1, -1):
        completion_string += char_map[left_string[i]]
    return completion_string


def calculate_score(completion_string):
    score = 0
    for char in completion_string:
        score *= 5
        if char == ')':
            score += 1
        elif char == ']':
            score += 2
        elif char == '}':
            score += 3
        elif char == '>':
            score += 4
    return score


with open("input.txt") as f:
    for line in f:
        is_corrupted = False
        left = ""
        right = ""
        for char in line.rstrip():
            if char == '(' or char == '[' or char == '{' or char == '<':
                left += char
            else:
                right += char
                if char != char_map[left[-1]]:
                    is_corrupted = True
                else:
                    left = left[:-1]
        if not is_corrupted:
            completion_strings.append(build_completion_string(left))
    print(completion_strings)

scores = [calculate_score(c) for c in completion_strings]
print(sorted(scores)[int(len(scores)/2)])
