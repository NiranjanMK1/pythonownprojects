import re
prog = re.compile(r'm\w\w')

a = 'cat mat rat'

result = prog.search(a)
print(result.group())
