import time
map = [x.split(',') for x in open("map_4.csv").read().strip().split('\n')]

map_dict = {}
DX = {1: 1, 2: -2, 3: 1, 4: 0}
DY = {1: 0, 2: 0, 3: -1, 4: 2}

length = len(map)
width = len(map[0])
for i in range(length):
    for j in range(width):
        map_dict[(j, i)] = map[i][j]

start_position = 0
end_position = 0
walls = set()
footpath = set()
for key, value in map_dict.items():
    if value == '0':
        footpath.add(key)
    elif value == '2':
        start_position = key
    elif value == '3':
        end_position = key
footpath.add(end_position)

find = False


def next_points(actually_points, length):
    help_dict = {}
    length += 1
    for position in actually_points:
        for i in range(1, 5):
            position = [position[0], position[1]]
            x = 0
            y = 0
            x += DX[i]
            y += DY[i]
            position[0] += x
            position[1] += y
            if (position[0], position[1]) in footpath:
                help_dict[(position[0], position[1])] = length
                footpath.remove((position[0], position[1]))
    return help_dict, length


if __name__ == '__main__':
    start = time.time()
    all_positions_dict = {}
    all_positions_dict[start_position] = 0
    length = 0
    find = False
    points, length = next_points(all_positions_dict, length)
    for key, value in points.items():
        all_positions_dict[key] = value

    while True:
        points, length = next_points(points, length)
        for key, value in points.items():
            all_positions_dict[key] = value
        if end_position in points:
            print("The shortest length: ",length)
            break
    end_value = all_positions_dict.get(end_position)
    start_value = all_positions_dict.get(start_position)
    step = 0
    point = [end_position[0], end_position[1]]
    end_program = False

    file = open("map_4_solution.csv", "w")
    good_road = []
    good_road.append(end_position)
    print(end_position)
    while True:
        step += 1
        for i in range(1, 5):
            x = 0
            y = 0
            x += DX[i]
            y += DY[i]
            point[0] += x
            point[1] += y
            if (point[0], point[1]) in all_positions_dict:
                if all_positions_dict[point[0], point[1]] == end_value - step:
                    help_var = [point[0],point[1]]
                    good_road.append(help_var)
                    print(good_road)
                    break
            if point == [start_position[0],start_position[1]]:
                end_program = True
                break
        if end_program == True:
            break
    good_road.reverse()
    for point in good_road:
        file.write("%d,%d\n" % (point[0],point[1]))
    stop = time.time()
    print("Time: ",stop-start)

