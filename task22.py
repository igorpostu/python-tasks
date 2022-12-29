categories = {'other': 0}

with open("task22_data.txt", 'r') as f:
    line = f.readline()
    while line != '':
        if line[0:1] == '/' and line[2:3] == '/' and line[-5:-1] == '.jpg':
            if line [1:2] not in categories:
                categories[line[1:2]] = 1
            else: categories[line[1:2]] += 1
        else: categories['other'] += 1
        line = f.readline()

for category in categories:
    print(category + ':', categories[category])