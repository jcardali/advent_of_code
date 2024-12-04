MUL_PATTERN = r'mul\(\d{1,3},\d{1,3}\)'
DO_PATTERN = r'do\()'
DONT_PATTERN = r'don\'t\()'

def do_mul(match):
    match = match.replace("mul(", "").replace(")", "")
    split = match.split(",")
    return int(split[0])*int(split[1])