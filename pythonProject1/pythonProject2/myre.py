import re


a = 'cat mat rat mop'

result = re.search(r"m\w\w",a)
print(result.group())
result2 = re.findall(r"m\w\w",a)

print(result2)
result3 = re.match(r"c\w\w",a)
print(result3.group())