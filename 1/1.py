maxcal = []
n = 0
maxcal.append(n)

with open('input.txt', encoding='utf-8') as data:
    for line in data:
        if line == '\n': 
            n += 1
            maxcal.append(n)
            print(maxcal)
            maxcal[n] = 0
        else:
            maxcal[n] += int(line)
            print(maxcal[n])
print(maxcal)
maxcal.sort(reverse=True)
print(maxcal)