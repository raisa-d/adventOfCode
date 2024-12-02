from pathname import pathname

# read data file into program
with open(pathname, 'r') as file:
    data = []
    # add each line as a nested array in data
    for line in file:
        line = line.replace('\n', '')
        line = line.split('   ')
        data.append(line)

file.close()

def total_distance(data):
    left = []
    right = []
    # create left and right side
    for row in data:
        left.append(row[0])
        right.append(row[1])
    
    # sort each side's data
    for side in [left, right]:
        side.sort()

    result = 0
    # compare each number's difference
    for i in range(0, len(left)):
        difference = abs(int(left[i]) - int(right[i]))
        # add to result
        result += difference
    
    return result

print(total_distance(data)) # 1223326