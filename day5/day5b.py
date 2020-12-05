def getMaxId(seats):
    max = 0
    ids = []
    for seat in seats:
        rowString = seat[0 : 7]
        columnString = seat[7 :]
        rowRange = [0, 127]
        columnRange = [0, 7]
        row = calculate(rowString, rowRange)
        column = calculate(columnString, columnRange)
        ids.append((row * 8) + column)
    ids.sort()

    for i in range(1, len(ids)-1):
        if(ids[i]+2 == ids[i+1]):
            return ids[i]+1
            
    return None

def calculate(string, range):
    for c in string:
            if c == 'F' or c == 'L':
                range[1] = range[0] + ((range[1] - range[0])//2)
            if c == 'B' or c == 'R':
                range[0] = range[1] - ((range[1] - range[0])//2)
    return range[0]


f = open('/home/bram/code/adventOfCode2020/day5/input.txt', 'r')
content = []
for line in f:
    content.append(line.strip())

print(getMaxId(content))