import re

txt = str(input())

x = re.findall('[A-Z][^A-Z]*', txt)

x = ' '.join(x)

x = x.lower()

x = re.sub("\s", "_", x)

print(x)