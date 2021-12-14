from shared import parse_input, fold

points, folds = parse_input()

fold(points, [folds[0]])

print(len(points))
