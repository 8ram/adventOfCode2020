def countTrees(lines):
    count = 0
    x = 0
    for i in range(len(lines)):
        x = (i * 3) % len(lines[i])
        if(lines[i][x] == "#"):
            lines[i][x] = "X"
            count += 1
        lines[i][x] = "O"
    return count


f = open('/home/bram/code/adventOfCode2020/day3/input.txt', 'r')
content = []
for line in f:
    content.append(list(line.strip()))

print(countTrees(content))