import random

#Functions:

def mine_generator (rows, columns, number_of_mines):
    grid_size = rows * columns
    mine_placement = []
    if number_of_mines < grid_size:
        while len(mine_placement) < number_of_mines:
            position = [random.randint(0, int(rows)-1), random.randint(0, int(columns)-1)]
            if not position in mine_placement:
                mine_placement.append(position)
    return mine_placement

def grid_generator (rows, columns, mine_placement):
    initial_grid = [[0 for column in range(columns)] for row in range(rows)]
    final_grid = [[0 for column in range(columns)] for row in range(rows)]
    for mine in mine_placement:
        final_grid[mine[0]][mine[1]] = "x"
        if mine[0] == 0 and mine[1] == 0:
            initial_grid[mine[0]][mine[1]+1] += 1
            initial_grid[mine[0]+1][mine[1]+1] += 1
            initial_grid[mine[0]+1][mine[1]] += 1
        elif mine[0] == 0 and mine[1] == columns - 1:
            initial_grid[mine[0]][mine[1]-1] += 1
            initial_grid[mine[0]+1][mine[1]-1] += 1
            initial_grid[mine[0]+1][mine[1]] += 1
        elif mine[0] == rows - 1 and mine[1] == 0:
            initial_grid[mine[0]-1][mine[1]] += 1
            initial_grid[mine[0]-1][mine[1]+1] += 1
            initial_grid[mine[0]][mine[1]+1] += 1
        elif mine[0] == rows -1 and mine[1] == columns - 1:
            initial_grid[mine[0]-1][mine[1]] += 1
            initial_grid[mine[0]-1][mine[1]-1] += 1
            initial_grid[mine[0]][mine[1]-1] += 1
        elif mine[0] == 0:
            initial_grid[mine[0]][mine[1]-1] += 1
            initial_grid[mine[0]][mine[1]+1] += 1
            initial_grid[mine[0]+1][mine[1]-1] += 1
            initial_grid[mine[0]+1][mine[1]] += 1
            initial_grid[mine[0]+1][mine[1]+1] += 1
        elif mine[0] == rows - 1:
            initial_grid[mine[0]][mine[1]-1] += 1
            initial_grid[mine[0]][mine[1]+1] += 1
            initial_grid[mine[0]-1][mine[1]-1] += 1
            initial_grid[mine[0]-1][mine[1]] += 1
            initial_grid[mine[0]-1][mine[1]+1] += 1
        elif mine[1] == 0:
            initial_grid[mine[0]-1][mine[1]] += 1
            initial_grid[mine[0]-1][mine[1]+1] += 1
            initial_grid[mine[0]][mine[1]+1] += 1
            initial_grid[mine[0]+1][mine[1]] += 1
            initial_grid[mine[0]+1][mine[1]+1] += 1
        elif mine[1] == columns - 1:
            initial_grid[mine[0]-1][mine[1]] += 1
            initial_grid[mine[0]-1][mine[1]-1] += 1
            initial_grid[mine[0]][mine[1]-1] += 1
            initial_grid[mine[0]+1][mine[1]] += 1
            initial_grid[mine[0]+1][mine[1]-1] += 1
        else:
            initial_grid[mine[0]-1][mine[1]-1] += 1
            initial_grid[mine[0]-1][mine[1]] += 1
            initial_grid[mine[0]-1][mine[1]+1] += 1
            initial_grid[mine[0]][mine[1]-1] += 1
            initial_grid[mine[0]][mine[1]+1] += 1
            initial_grid[mine[0]+1][mine[1]-1] += 1
            initial_grid[mine[0]+1][mine[1]] += 1
            initial_grid[mine[0]+1][mine[1]+1] += 1
    row_num = 0
    for row in final_grid:
        column_num = 0
        for column in row:
            if row[column_num] != "x":
                row[column_num] = initial_grid[row_num][column_num]
            column_num += 1
        row_num += 1
    return final_grid

def display_grid_generator (rows, columns):
    display_grid = [[" " for column in range(columns)] for row in range(rows)]
    return display_grid

def terminal_interface(display_grid, number_of_mines):
    title = "\n     "
    for index in range(int(len(display_grid[0])*2/5)):
        title += "    "
    title += "MINE SWEEPER"
    print(title)
    print("{} flags remaining".format(number_of_mines))
    top_line = "    "
    first_row = "    "
    for index in range(len(display_grid[0])):
        if index + 1 > 9:
            top_line += " {index}  ".format(index = index + 1)
        elif index + 1 < 10:
            top_line += "  {index}  ".format(index = index + 1)
        first_row += " ___ "
    print(top_line)
    print(first_row)
    for index in range(len(display_grid)):
        if index + 1 > 9:
            top_side = "    "
            mid_side = " {} ".format(index+1)
            bot_side = "    "
        elif index + 1 < 10:
            top_side = "    "
            mid_side = "  {} ".format(index+1)
            bot_side = "    "
        for listed_index in range(len(display_grid[index])):
            top_side += "|   |"
            mid_side += "| {} |".format(display_grid[index][listed_index])
            bot_side += "|___|"
        print(top_side)
        print(mid_side)
        print(bot_side)

def game_generate_input():
    rows = input("How many rows would you like to play on (Between 3 and 20)?")
    try:
        if not 2 < int(rows) < 21:
            print("Number is not valid")
            x = game_generate_input()
            return x
    except ValueError:
        print("Not a valid input")
        x = game_generate_input()
        return x
    columns = input("How many columns would you like to play on (Between 3 and 20)?")
    try:
        if not 2 < int(columns) < 21:
            print("Number is not valid")
            x = game_generate_input()
            return x
    except ValueError:
        print("Not a valid input")
        x = game_generate_input()
        return x
    mines = input ("How many mines would you like to have in the game?")
    try:
        if int(mines) < 1: 
            print("You need atleast 1 mine in the game")
            x = game_generate_input()
            return x
        elif int(mines) > (int(rows) * int(columns)):
            print("Too Many Mines!!!")
            x = game_generate_input()
            return x
    except ValueError:
        print("Not a valid input")
        x = game_generate_input()
        return x
    return_list = [int(rows), int(columns), int(mines)]
    return return_list

def user_input(start_grid):
    print("\nWhat would you like to do?")
    print("(1) Reveal coordinates")
    print("(2) Flag / Unflag coordinates")
    print("(3) End the game")
    try:
        user_decision = int(input())
        if user_decision == 1:
            x = reveal_coordinates()
            x.append(1)
            if x[0] >= len(start_grid) or len(x) < 3:
                print("invalid coordinates")
                x = user_input(start_grid)
            elif x[1] >=  len(start_grid[0]) or len(x) < 3:
                print("invalid coordinates")
                x = user_input(start_grid)              
            return x
        elif user_decision == 2:
            x = flag_coordinates()
            x.append(2)
            if x[0] >= len(start_grid) or len(x) < 3 or isinstance(x[0], str):
                print("invalid coordinates")
                x = user_input(start_grid)
            elif x[1] >=  len(start_grid[0]) or len(x) < 3 or isinstance(x[1], str):
                print("invalid coordinates")
                x = user_input(start_grid)    
            return x
        elif user_decision == 3:
            return [0, 0, 3]
        else:
            print("invalid number")
            x = user_input(start_grid)
            return x
    except:
        print("invalid number")
        x = user_input(start_grid)
        return x

def reveal_coordinates():
    coords = input("Type in coordinates that you would like to input (e.g \"2 3\"):")
    list_coords = coords.split()
    list_coords_2 = []
    for number in list_coords:
        list_coords_2.append(int(number)-1)
    return list_coords_2

def flag_coordinates():
    coords = input("Type in coordinates that you would like to flag (e.g \"2 3\"):")
    list_coords = coords.split()
    list_coords_2 = []
    for number in list_coords:
        list_coords_2.append(int(number)-1)
    return list_coords_2

def game_running (start_grid, interface_grid, number_of_flags, number_of_mines):
    win_con = 0
    for row in interface_grid:
        win_con += row.count(" ")
    if win_con - number_of_flags  == 0:
        print("You win!")
    else:
        action = user_input(start_grid)
        if action[2] == 1:
            if start_grid[action[0]][action[1]] == "x":
                interface_grid[action[0]][action[1]] = "x"
                terminal_interface(interface_grid, number_of_flags)
                print("Game Over")
            elif start_grid[action[0]][action[1]] > 0 and interface_grid[action[0]][action[1]]  == "F":
                new_number_of_flags = number_of_flags + 1
                interface_grid[action[0]][action[1]] = start_grid[action[0]][action[1]]
                print(new_number_of_flags)
                terminal_interface(interface_grid, new_number_of_flags)
                game_running(start_grid, interface_grid, new_number_of_flags, number_of_mines)
            elif start_grid[action[0]][action[1]] == 0 and interface_grid[action[0]][action[1]]  == "F":
                new_number_of_flags = number_of_flags + 1
                interface_grid[action[0]][action[1]] = start_grid[action[0]][action[1]]
                reveal_expansion(start_grid, interface_grid, action[0], action[1])
                terminal_interface(interface_grid, new_number_of_flags)
                game_running(start_grid, interface_grid, new_number_of_flags, number_of_mines)
            elif start_grid[action[0]][action[1]] > 0:
                interface_grid[action[0]][action[1]] = start_grid[action[0]][action[1]]
                terminal_interface(interface_grid, number_of_flags)
                game_running(start_grid, interface_grid, number_of_flags, number_of_mines)
            elif start_grid[action[0]][action[1]] == 0:
                interface_grid[action[0]][action[1]] = start_grid[action[0]][action[1]]
                reveal_expansion(start_grid, interface_grid, action[0], action[1])
                terminal_interface(interface_grid, number_of_flags)
                game_running(start_grid, interface_grid, number_of_flags, number_of_mines)
        elif action[2] == 2:
            if interface_grid[action[0]][action[1]] == "F":
                interface_grid[action[0]][action[1]] = " "
                new_number_of_flags = number_of_flags + 1
                terminal_interface(interface_grid, new_number_of_flags)
                game_running(start_grid, interface_grid, new_number_of_flags, number_of_mines)
            elif interface_grid[action[0]][action[1]] == " " and number_of_flags > 0:
                interface_grid[action[0]][action[1]] = "F"
                print(interface_grid[action[0]][action[1]])
                new_number_of_flags = number_of_flags - 1
                terminal_interface(interface_grid, new_number_of_flags)
                game_running(start_grid, interface_grid, new_number_of_flags, number_of_mines)
            else:
                print("Unable to Flag")
                terminal_interface(interface_grid, number_of_flags)
                game_running(start_grid, interface_grid, number_of_flags, number_of_mines)
        elif action[2] == 3:
            terminal_interface(interface_grid, number_of_flags)
            print("Game Over")

def reveal_expansion (start_grid, interface_grid, row, column):
    try:
        if interface_grid[row -1][column - 1] == " " and row - 1 >= 0 and column - 1 >= 0:
            interface_grid[row -1][column - 1] = start_grid [row -1][column - 1]
            if interface_grid[row -1][column - 1] == 0:   
                reveal_expansion (start_grid, interface_grid, row -1, column - 1)
    except:
        None
    try:
        if interface_grid[row -1][column] == " " and row - 1 >= 0:
            interface_grid[row -1][column] = start_grid [row -1][column]
            if interface_grid[row -1][column] == 0:            
                reveal_expansion (start_grid, interface_grid, row -1, column)
    except:
        None
    try:
        if interface_grid[row -1][column +1] == " " and row - 1 >= 0:
            interface_grid[row -1][column +1] = start_grid [row -1][column +1]
            if interface_grid[row -1][column +1] == 0:
                reveal_expansion (start_grid, interface_grid, row -1, column +1)
    except:
        None
    try:
        if interface_grid[row][column -1] == " " and column -1 >= 0:
            interface_grid[row][column -1] = start_grid [row][column -1]
            if interface_grid[row][column -1] == 0:
                reveal_expansion (start_grid, interface_grid, row, column -1)
    except:
        None
    try:
        if interface_grid[row][column +1] == " ":
            interface_grid[row][column +1] = start_grid [row][column +1]
            if interface_grid[row][column +1] == 0:
                reveal_expansion (start_grid, interface_grid, row, column +1)
    except:
        None
    try:
        if interface_grid[row +1][column - 1] == " " and column -1 >= 0:
            interface_grid[row +1][column - 1] = start_grid [row +1][column - 1]
            if interface_grid[row +1][column - 1] == 0:
                reveal_expansion (start_grid, interface_grid, row +1, column - 1)
    except:
        None
    try:
        if interface_grid[row +1][column] == " ":
            interface_grid[row +1][column] = start_grid [row +1][column]
            if interface_grid[row +1][column] == 0:
                reveal_expansion (start_grid, interface_grid, row +1, column)
    except:
        None
    try:
        if interface_grid[row +1][column +1] == " ":
            interface_grid[row +1][column +1] = start_grid [row +1][column +1]
            if interface_grid[row +1][column +1] == 0:
                reveal_expansion (start_grid, interface_grid, row +1, column +1)
    except:
        None


#Main Code:

game_config = game_generate_input()
mines_in_game = mine_generator(game_config[0], game_config[1], game_config[2])
start_grid_1 = grid_generator(game_config[0], game_config[1], mines_in_game)
interface_grid_1 = display_grid_generator(game_config[0], game_config[1])
terminal_interface(interface_grid_1, game_config[2])
game_running(start_grid_1, interface_grid_1, game_config[2], game_config[2])
