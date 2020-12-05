def getMaxId(seats):
    max = 0
    for seat in seats:
        rowString = seat[0 : 7]
        columnString = seat[7 :]
        rowRange = [0, 127]
        columnRange = [0, 7]
        row = calculate(rowString, rowRange)
        column = calculate(columnString, columnRange)
        id = (row * 8) + column
        print("row: " + str(row) + " column: " + str(column) + " id: " + str(id))
        if(id > max):
            max = id
    return max

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