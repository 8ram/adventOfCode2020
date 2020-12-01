import time 
def Find2Values(arr):
    dict = {}
    for num in arr:
        if dict.get(2020-num) == 1:
            return (2020-num) * num
        dict.update({num: 1})

def Find3Values(arr):
    dict = {}
    for num in arr:
        dict.update({num: 1})
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if dict.get(2020-arr[i]-arr[j]) == 1:
                return (2020-arr[i]-arr[j]) * arr[i] * arr[j]

f = open('input.txt', 'r')
content = []
for line in f:
    content.append(int(line.strip()))

print(Find2Values(content))
print(Find3Values(content))
