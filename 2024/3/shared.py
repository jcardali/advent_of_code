MUL_PATTERN = r'mul\(\d{1,3},\d{1,3}\)'
MUL_DO_DONT_PATTERN = r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))'

def do_mul(match):
    match = match.replace("mul(", "").replace(")", "")
    split = match.split(",")
    return int(split[0])*int(split[1])