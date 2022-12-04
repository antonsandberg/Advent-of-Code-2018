with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]


summa = 0
visited = set()
visited.add(0)
notFinished = True
while notFinished:
    for row in data:
        ope = row[0]
        if ope == "+":
            summa += int(row[1:])
        else:
            summa -= int(row[1:])
        if summa in visited:
            print(summa)
            notFinished = False
        visited.add(summa)
