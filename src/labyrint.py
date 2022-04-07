import random

START = 12
FINISH = 24
ROAD = 1
WALL = 0

map = [
    [START, ROAD, ROAD, ROAD, ROAD],
    [WALL, WALL, WALL, WALL, ROAD],
    [WALL, WALL, WALL, WALL, ROAD],
    [WALL, WALL, WALL, WALL, ROAD],
    [WALL, WALL, WALL, WALL, FINISH]
]

start_pos_x = 0 
start_pos_y = 0

y_rows = 5
x_columns = 5

def get_next_free_position(current_position_y, current_position_x):
    random_number = random.random()

    can_go_right = current_position_x+1 < x_columns and map[current_position_y][current_position_x+1] == ROAD
    can_go_left = current_position_x-1 > 0 and map[current_position_y][current_position_x-1] == ROAD
    can_go_bottom = current_position_y+1 < y_rows and map[current_position_y+1][current_position_x] == ROAD
    can_go_top = current_position_y-1 > 0 and map[current_position_y-1][current_position_x] == ROAD

    if can_go_right:
        print("can go right")
        return [current_position_y, current_position_x+1]

    if can_go_left:
        print("can go left")
        return [current_position_y, current_position_x-1]

    if can_go_bottom:
        print("can go bottom")
        return [current_position_y+1, current_position_x]

    if can_go_top:
        print("can go top")
        return [current_position_y-1, current_position_x]

next_free_position = get_next_free_position(start_pos_y, start_pos_x)
print("Next free position is: ", next_free_position)

while next_free_position:
    print("Next free position is: ", next_free_position)
    next_free_position = get_next_free_position(next_free_position[0], next_free_position[1])
