import re
def insert_spaces(s):
    return re.sub(r'([A-Z])', r' \1', s).strip()

s = input()
wr = insert_spaces(s)
print(wr)