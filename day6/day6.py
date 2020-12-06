def calculate(lines):
    buffer = []
    sum = 0
    for line in lines:
        if len(line) == 0:
            sum += len(buffer)
            buffer = []
        for c in line:
            if c not in buffer:
                buffer.append(c)
    sum += len(buffer)
    return sum

f = open('/home/bram/code/adventOfCode2020/day6/input.txt', 'r')
content = []
for line in f:
    content.append(line.strip())

print(calculate(content))