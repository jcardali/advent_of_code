def do_mul(match):
    match = match.replace("mul(", "").replace(")", "")
    split = match.split(",")
    return int(split[0])*int(split[1])