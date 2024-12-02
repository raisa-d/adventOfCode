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

def similarity_score(data):
    # create left and right side of list
    left = []
    right = []
    for row in data:
        left.append(row[0])
        right.append(row[1])

    count = {}

    # loop thru unique left side, fill in count object
    unique_left = set(left)
    for num in unique_left:
        count[num] = 0

    # loop thru right side, check if key in object. if yes, add 1
    for num in right:
        if num in count:
            count[num] += 1

    result = 0
    # loop thru left side, multiply each num by its count, add to result
    for num in left:
        result += int(num) * int(count[num])
    
    return result

answer = similarity_score(data)
print(answer) # CORRECT ANSWER: 21070419