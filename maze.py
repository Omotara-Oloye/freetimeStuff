import random 
from collections import deque


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def generate_maze(width, height):
    grid = [[set() for _ in range(width)] for _ in range(height)]
    visited = [[False for _ in range(width)] for _ in range(height)]


    stack = []
    start = (0,0)
    visited[start[0]][start[1]] = True
    stack.append(start)


    while stack:
        current_row, current_col = stack[-1] #peek at top of stack

        #find unvisited neighbors of the cell we are currently on
        unvisted_neighbors = []
        for row_direction, col_direction in DIRECTIONS:
            next_row, next_col = current_row + row_direction, current_col + col_direction
            #check bounds
            if 0 <= next_row < height and 0 <= next_col < width and not visited[next_row][next_col]:
                unvisted_neighbors.append((row_direction,col_direction))
        if unvisted_neighbors:
            #Pick random direction to remove bias
            row_direction, col_direction = random.choice(unvisted_neighbors)
            next_row, next_col = current_row + row_direction, current_col + col_direction   

            grid[current_row][current_col].add((row_direction, col_direction))
            #Negate in order to get the reserve direction for backtracking for walls
            grid[next_row][next_col].add((-row_direction, - col_direction))

            visited[next_row][next_col] = True
            stack.append((next_row, next_col))

        else:
            stack.pop()

    return grid   

def render_maze(grid, height, width, path = None):   
    #double to show the cell and potential wall
    canvas_height = height * 2 + 1
    canvas_width = width * 2 + 1

    canvas = [['#' for _ in range(canvas_width)] for _ in range(canvas_height)]
    
    #Carve each cell
    for row in range(height):
        for col in range(width):
            canvas[row * 2 + 1][col * 2 + 1] = '.'
    #Carve each pathway between cells
    for row in range(height):
        for col in range(width):
            for row_direction, col_direction in grid[row][col]:
                canvas[row * 2 + 1 + row_direction][col * 2 + 1 + col_direction] = '.'

    #Overlay solved path
    if path:
        for row, col in path:
            canvas[row * 2 + 1][col * 2 + 1] = '*'
        for i in range(len(path) - 1):
            r1, c1 = path[i]
            r2, c2 = path[i + 1]
            mid_row = r1 * 2 + 1 + (r2 - r1)
            mid_col = c1 * 2 + 1 + (c2 - c1)
            canvas[mid_row][mid_col] = '*'            

    canvas[1][1] = "S"
    canvas[(height - 1) * 2 + 1][(width - 1) * 2 + 1] = "E"                

    return '\n'.join(''.join(row) for row in canvas)

def solve_maze(grid, height, width, start = (0,0), end = None):
    if end is None:
        end = (height - 1, width - 1)

    queue = deque()
    queue.append(start)
    past_steps = {start: None}

    while queue:
        current_step = queue.popleft()

        if current_step == end:
            break #we're at the end!

        current_row, current_col = current_step
        for row_direction, col_direction in grid[current_row][current_col]:  
            neighbor = (current_row + row_direction, current_col + col_direction)
            if neighbor not in past_steps:
                past_steps[neighbor] = current_step
                queue.append(neighbor)
    if end not in past_steps:
        return None

    #Construct pathway by walking backwards
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = past_steps[node]
    #Reverse path to start at beginning    
    path.reverse()

    return path    


       