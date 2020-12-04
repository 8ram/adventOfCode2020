def checkPassport(content):
    counter = 0
    keyBuffer = ""
    dataBuffer = ""
    passport = {}
    pCounter = 0
    for i in range(len(content)):
        if len(content[i]) == 0:
            if checkKeys(passport):
                counter += 1
            pCounter += 1
            passport = {}
        key = True
        keyBuffer = ""
        dataBuffer = ""
        j = 0
        while j < len(content[i]):
            if(content[i][j] == ' '):
                passport.update({keyBuffer: dataBuffer})
                keyBuffer = ""
                dataBuffer = ""
                key = True  # key mode
            elif(content[i][j] == ':'):
                key = False
            else:
                if key:
                    keyBuffer += content[i][j]
                else:
                    dataBuffer += content[i][j]
            j += 1
        passport.update({keyBuffer: dataBuffer})

    if checkKeys(passport):
        counter += 1
    return counter


def checkKeys(passport):
    validKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in validKeys:
        if key not in passport:
            return False
        elif key == "byr" and not (1920 <= int(passport[key]) <= 2002):
            return False
        elif key == "iyr" and not (2010 <= int(passport[key]) <= 2020):
            return False
        elif key == "eyr" and not (2020 <= int(passport[key]) <= 2030):
            return False
        elif key == "hgt":
            value = ["", ""]
            unitMode = False
            for c in passport[key]:
                if c == 'i' or c == 'c' or unitMode:
                    unitMode = True
                    value[1] += c
                else:
                    value[0] += c
            value[0] = int(value[0])
            if value[1] == "cm":
                if not (150 <= value[0] <= 193):
                    return False
            elif value[1] == 'in':
                if not (59 <= value[0] <= 76):
                    return False
            else:
                return False
        elif key == "hcl":
            for i in range(len(passport[key])):
                if(i == 0):
                    if(passport[key][0] != "#"):
                       return False
                elif not ((ord('a') <= ord(passport[key][i]) <= ord('z')) or (ord('0') <= ord(passport[key][i]) <= ord('9'))):
                    return False
        elif key == "ecl":
            valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if passport[key] not in valid:
                return False
        elif key == "pid":
            if len(passport[key]) != 9 or not passport[key].isnumeric():
                return False
    return True

f = open('input.txt', 'r')
content = []
for line in f:
    content.append(line.strip())

print(checkPassport(content))
