def generateMatrix(n):
    Map = [[None for i in range(n + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        Map[i][0] = -1
        Map[i][n] = -1
        Map[0][i] = -1
        Map[n][i] = -1

    def sl(direction, position, mark):
        if Map[position[0]][position[1]] is not None:
            return Map
        while position[0] <= n and position[1] <= n and Map[position[0]][position[1]] is None:
            if direction == 1:
                Map[position[0]][position[1]] = mark
                position[0] += 1
            elif direction == 0:
                Map[position[0]][position[1]] = mark
                position[1] += 1
            elif direction == 3:
                Map[position[0]][position[1]] = mark
                position[0] -= 1
            elif direction == 2:
                Map[position[0]][position[1]] = mark
                position[1] -= 1
            mark += 1
        if direction == 0:
            position[1] -= 1
            position[0] += 1
        elif direction == 1:
            position[0] -= 1
            position[1] -= 1
        elif direction == 2:
            position[1] += 1
            position[0] -= 1
        elif direction == 3:
            position[0] += 1
            position[1] += 1
        return sl((direction + 1) % 4, position, mark)

    tmp = sl(0, [1, 1], 1)
    result = [tmp[i][1:n] for i in range(1,n)]
    return result


print generateMatrix(3)
