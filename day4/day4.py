def checkPassport(content):
    counter = 0
    passport = {}
    for i in range(len(content)):
        if len(content[i]) == 0:
            if checkKeys(passport):
                counter += 1
            passport = {}
        read = True
        j = 0
        buffer = ""
        while j < len(content[i]):
            if(j>0 and content[i][j-1] == ' '):
                read = True
            if(content[i][j] == ':'):
                read = False
            if read:
                buffer += content[i][j]
            elif buffer!= '':
                passport.update({buffer: 1})
                buffer = ""
                j += 1 #skip space
            j+=1
    if checkKeys(passport):
                counter += 1
    return counter


def checkKeys(passport):
    validKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in validKeys:
        if key not in passport:
            return False
    return True


f = open('input.txt', 'r')
content = []
for line in f:
    content.append(list(line.strip()))

print(checkPassport(content))