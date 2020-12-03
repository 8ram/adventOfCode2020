import re
def run(strings):
    correct = 0
    regex = re.compile("(\d+)-(\d+) (.): (.+)")
    for i in strings:
        parts = regex.match(i).groups()
        num_char = parts[3].count(parts[2])
        if num_char in range(int(parts[0]), int(parts[1])+1):
            correct += 1
    return correct


f = open('input.txt', 'r')
content = []
for line in f:
    content.append(line.strip())

print(run(content))