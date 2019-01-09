total_data = [2,3,5,7,11,13,17,19,23,29,97,31,37,41,43,47,53,59,61,71,73,79,83,89]


def qsort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less, equal, more = [],[],[]
        for index in range(len(data)):
            if pivot > data[index]:
                less.append(data[index])
            elif pivot < data[index]:
                more.append(data[index])
            else:
                equal.append(data[index])
        return qsort(less) + equal + qsort(more)

print(qsort(total_data))