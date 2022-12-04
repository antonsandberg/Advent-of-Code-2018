with open('input.txt') as f:
    data = f.read().strip()

# data = "dabAcCaCBAcCcaDA"

changes = 1
new_data = data

counter = 0
while changes:
    counter += 1
    changes = 0
    remove_indices = []
    data = new_data
    for i in range(len(data)-1):
        a = data[i]
        b = data[i+1]
        if [i-1, i] in remove_indices:
            continue
        elif (a.lower() == b.lower()) and \
        ((a.islower() and b.isupper()) or (a.isupper() and b.islower())):
            changes += 1
            remove_indices.append(i)
            remove_indices.append(i+1)
    
    if counter % 1 == 0:
        print(f'Iteration {counter}')
    new_data = "".join([char for (i, char) in enumerate(data) if i not in remove_indices])
print(f'Day 5 part 1: {len(new_data)-1}')
