def recursive(rules, search):
    if len(rules[search]) == 0:
        # nothing found
        return False
    if 'shiny gold' in rules[search].keys():
        # found
        return True
    else:
        #recurse deeper
        for thing in rules[search]:
            if recursive(rules, thing):
                return True

def recursive2(rules, color):
    sum = 0
    if len(rules[color]) == 0:
        return 0
    for key, value in rules[color].items():
        sum += value + value * recursive2(rules, key)
    return sum

def getRules(rules):
    RuleData = {}
    for rule in rules:
        buffer = ""
        for i in range(len(rule)):
            if i < 2:
                if i == 1:
                    buffer += " "
                buffer += rule[i]
            if i == 2:
                key = buffer
                buffer = ""
            if i == 4:
                RuleData[key] = fits(rule[i:])
    return RuleData

def fits(data):
    color = ""
    num = -1
    rules = {}
    for i in range(len(data)):
        if i%4 == 0:
            if data[i] == 'no':
                return rules
            num = int(data[i])
        if i%4 == 1 or i%4 == 2:
            if i%4 == 2:
                    color += " "
            color += data[i]
        if i%4 == 3:
            rules[color] = num
            color = ""
            num = -1
    return rules

f = open('/home/bram/code/adventOfCode2020/day7/input.txt', 'r')
content = []
for line in f:
    content.append(line.strip().split(' '))

rules = getRules(content)
count = 0
for item in rules:
    if recursive(rules, item):
        count += 1

print(count)
print(recursive2(rules, "shiny gold"))