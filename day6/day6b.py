def calculate(lines):
    buffer = []
    sum = 0
    i = -1
    for line in lines:
        if len(line) == 0:
            # TODO: change this
            sum += intersection(buffer)
            buffer = []
            i = -1
        else:
            buffer.append([])
            i += 1
        for c in line:
            if c not in buffer:
                buffer[i].append(c)
    sum += len(buffer)
    return sum

def intersection(data):
    for i in range(1, len(data)):
        data[0] = list(set(data[0]).intersection(data[i]))

    return len(data[0])


f = open('/home/bram/code/adventOfCode2020/day6/input.txt', 'r')
content = []
for line in f:
    content.append(line.strip())

print(calculate(content))