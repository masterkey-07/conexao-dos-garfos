from os import system
from itertools import combinations

colors = []

print("Add 4 colors for the cubes:")
for i in range(1, 5):
    colors.append(input('Add color: '))

cubes = []

for i in range(1, 5):
    cube = []

    print(f'\nCube {i} colors:')
    print(f'Available colors: {", ".join(colors)}')
    print('Please enter the colors for each face of the cube.')
    print('North, South, East, West, Top, Bottom')

    color1 = input(f'\nAdd north color for cube {i}: ')
    color2 = input(f'\nAdd south color for cube {i}: ')
    color3 = input(f'\nAdd east color for cube {i}: ')
    color4 = input(f'\nAdd west color for cube {i}: ')
    color5 = input(f'\nAdd top color for cube {i}: ')
    color6 = input(f'\nAdd bottom color for cube {i}: ')

    cube.append((color1, color2))  # North-South
    cube.append((color3, color4))  # East-West
    cube.append((color5, color6))  # Top-Bottom
    
    cubes.append(cube)

system('clear')

edges = []

for idx, cube in enumerate(cubes):
    for pair in cube:
        edges.append((pair[0], pair[1], idx + 1))  

def edges_for_cube(subset):
    return set([a[2] for a in subset])

def node_degree(subset):
    degree = {}
    for a in subset:
        for color in [a[0], a[1]]:
            degree[color] = degree.get(color, 0) + 1
    return degree

def valid_degree(subset):
    degree = node_degree(subset)
    return all(v == 2 for v in degree.values())

def solve_cube_problem(edges):
    solutions = []

    for first_solution in combinations(edges, 4):
        if len(edges_for_cube(first_solution)) != 4:
            continue
        if not valid_degree(first_solution):
            continue

        left = [edge for edge in edges if edge not in first_solution]

        for second_solution in combinations(left, 4):
            if len(edges_for_cube(second_solution)) != 4:
                continue
            if not valid_degree(second_solution):
                continue

            solutions.append((first_solution, second_solution))

    return solutions

solutions = solve_cube_problem(edges)

face_names = ['North-South', 'East-West', 'Top-Bottom']

def build_column(subgraph, face:int):
    cubes_dict = {i: {} for i in range(1, 5)}
    
    for edge in subgraph:
        color1, color2, idx = edge
        available_faces = [f for f in face_names if f not in cubes_dict[idx]]
    
        if available_faces:
            turn = False

            for index in range(1, idx):
                if cubes_dict[index][available_faces[face]][0] == color1 or cubes_dict[index][available_faces[face]][1] == color2:
                    turn = True
                    break

            if turn:
                cubes_dict[idx][available_faces[face]] = (color2, color1)
            else:
                cubes_dict[idx][available_faces[face]] = (color1, color2)
    
    return cubes_dict

print('' + '-' * 50)

if solutions:
    for idx, (sub1, sub2) in enumerate(solutions):
        print(f"\nSolution {idx + 1}:")
        print("\tSubgraph 1:", sub1)
        print("\tSubgraph 2:", sub2)

        print("\nColumn of blocks for Subgraph 1:")
        cubes1 = build_column(sub1,0)
        for i in range(1, 5):
            print(f" Block {i}:")
            for face in face_names:
                if face in cubes1[i]:
                    print(f"   {face}: {cubes1[i][face][0]} - {cubes1[i][face][1]}")

        print("\nColumn of blocks for Subgraph 2:")
        cubes2 = build_column(sub2, 1)
        for i in range(1, 5):
            print(f" Block {i}:")
            for face in face_names:
                if face in cubes2[i]:
                    print(f"   {face}: {cubes2[i][face][0]} - {cubes2[i][face][1]}")

        print('' + '-' * 50)
else:
    print("No solution found.")
