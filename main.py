def get_data():
    e_data = []
    with open("input.txt") as iFile:
        while True:
            line = iFile.readline()
            if not line:
                break
            temp = (line[:len(line)] + line[len(line) + 1:]).split()
            for x in range(len(temp)):
                temp[x] = int(temp[x])
            e_data.append(temp)
            print(line, end='')
        print()
    return e_data


def dfsr(adjacency_matrix_my, s, heights, label):
    heights[s][0] = True
    for k in range(len(adjacency_matrix_my)):
        if adjacency_matrix_my[s][k] == 1 and heights[k][0] == False:
            label=dfsr(adjacency_matrix_my, k, heights, label)
    heights[s][1] = label
    return label - 1


def create_adjacency_matrix(e_data):
    matrix = [0] * e_data[0][0]
    for x in range(e_data[0][0]):
        matrix[x] = [0] * e_data[0][0]

    for y in range(1, len(e_data)):
        matrix[e_data[y][0] - 1][e_data[y][1] - 1] = 1
    return matrix


def create_result_of_topological_sort(heights):
    path = []
    for k in range(len(heights)):
        for j in range(len(heights)):
            if (k+1) == heights[j][1]:
                path.append(j + 1)
                break
    return path


def topological_sort(adjacency_matrix_my):
    heights = []
    for x in range(len(adjacency_matrix_my)):
        temp = []
        temp.append(False)
        temp.append(0)
        heights.append(temp)
    current_label = len(adjacency_matrix_my)
    for v in range(len(heights)):
        if heights[v][0] == False:
            current_label = dfsr(adjacency_matrix_my, v, heights, current_label)
    return create_result_of_topological_sort(heights)


data = get_data()

pathMy = topological_sort(create_adjacency_matrix(data))
print(pathMy)
