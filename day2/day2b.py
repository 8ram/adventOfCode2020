import re
def run(strings):
    correct = 0
    regex = re.compile("(\d+)-(\d+) (.): (.+)")
    for i in strings:
        parts = regex.match(i).groups()
        first = int(parts[0])-1
        second = int(parts[1])-1
        if (parts[3][first] == parts[2] and parts[3][second] != parts[2]) or (parts[3][first] != parts[2] and parts[3][second] == parts[2]):
            correct += 1
    return correct


f = open('input.txt', 'r')
content = []
for line in f:
    content.append(line.strip())

print(run(content))