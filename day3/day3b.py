def countTrees(lines, right, down):
    count = 0
    x = 0
    y = 0
    for i in range(len(lines)):
        x = (i * right) % len(lines[i])
        y = (i * down)
        if(y >= len(lines)):
            break
        if(lines[y][x] == "#"):
            count += 1
    return count


f = open('/home/bram/code/adventOfCode2020/day3/input.txt', 'r')
content = []
for line in f:
    content.append(list(line.strip()))
    
print(countTrees(content, 3, 1))
print(countTrees(content, 1, 1) * countTrees(content, 3, 1) * countTrees(content, 5, 1) * countTrees(content, 7, 1) * countTrees(content, 1, 2))