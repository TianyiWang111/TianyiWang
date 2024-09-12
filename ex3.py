import random

# 1. Define the size of the grid
grid_size = 5  # Can be changed to any size

# 2. Assign the player and treasure random positions on the map
player_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
treasure_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]

# 3. Decide the maximum moves the player can make
max_moves = 10  # Maximum number of moves allowed

# Helper function to calculate distance
def calculate_distance(player, treasure):
    return abs(player[0] - treasure[0]) + abs(player[1] - treasure[1])

# 4. Calculate the initial distance between player and treasure
initial_distance = calculate_distance(player_position, treasure_position)

# 5. Start the game loop
moves_made = 0
while moves_made < max_moves:
    print(f"\nPlayer position: {player_position}")
    move = input("Enter your move (N, S, E, W): ").upper()

    if move == 'N':
        if player_position[1] > 0:
            player_position[1] -= 1
        else:
            print("Move not allowed, you are at the edge of the map.")
            continue
    elif move == 'S':
        if player_position[1] < grid_size - 1:
            player_position[1] += 1
        else:
            print("Move not allowed, you are at the edge of the map.")
            continue
    elif move == 'E':
        if player_position[0] < grid_size - 1:
            player_position[0] += 1
        else:
            print("Move not allowed, you are at the edge of the map.")
            continue
    elif move == 'W':
        if player_position[0] > 0:
            player_position[0] -= 1
        else:
            print("Move not allowed, you are at the edge of the map.")
            continue
    else:
        print("Invalid input. Please enter one of N, S, E, W.")
        continue

    # 5.1. Recalculate the player's distance from the treasure
    new_distance = calculate_distance(player_position, treasure_position)

    # 5.2 and 5.3. Tell the player if they're getting closer or farther
    if new_distance < initial_distance:
        print("You're getting closer!")
    elif new_distance > initial_distance:
        print("You're moving farther!")
    else:
        print("No change in distance.")

    initial_distance = new_distance

    # 5.5. Check if the player has found the treasure
    if player_position == treasure_position:
        print("Congratulations! You found the treasure!")
        break

    moves_made += 1
    print(f"Moves left: {max_moves - moves_made}")

# 5.6. If no more moves are possible
if moves_made == max_moves and player_position != treasure_position:
    print(f"Game over! You've used all your moves. The treasure was at {treasure_position}.")