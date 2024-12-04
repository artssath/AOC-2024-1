def read_data_list(file):
    input_data=[]
    data_to_dots=[]
    for line in open(file,'r').readlines():
        input_data.append(line.split('\n')[0])
        data_to_dots.append('.' * len(line.split('\n')[0]))
    return input_data,data_to_dots

def find_xmas_in_data(grid, word, data_to_dots):
    cols = len(grid[0])
    rows = len(grid)
    word_length = len(word)
    data_to_dots=list(data_to_dots)
    found_positions = []
    xmas_position_list=[]

    # Directions 
    directions = [ (0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1) ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                positions = []
                for k in range(word_length):
                    nr, nc = r + dr * k, c + dc * k
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == word[k]:
                        positions.append((nr, nc))
                    else:
                        break
                if len(positions) == word_length:
                    found_positions.append(positions)
                    xmas_position_list.extend(positions)
                    
    for cr, cc in xmas_position_list:
        list_row=list(data_to_dots[cr])
        list_row[cc] = grid[cr][cc]
        list_row = ''.join(list_row)
        data_to_dots[cr] = list_row
    return found_positions,data_to_dots


def find_xmas_in_x(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Iterate through the grid, avoiding the borders
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == 'A':    # Check char is "A"
                if ((grid[r - 1][c - 1] == 'M' and grid[r + 1][c + 1] == 'S') or (grid[r - 1][c - 1] == 'S' and grid[r + 1][c + 1] == 'M')) and ((grid[r - 1][c + 1] == 'M' and grid[r + 1][c - 1] == 'S') or (grid[r - 1][c + 1] == 'S' and grid[r + 1][c - 1] == 'M')) :
                    count += 1
    return count



# Example usage
if __name__ == "__main__":
    file_data,data_to_dots = read_data_list("input-4")
    x_word= "XMAS"
    results,changed_grid = find_xmas_in_data(file_data, x_word, data_to_dots)
    print(f'Keyword "{x_word}" was found {len(results)} times.')
    X_results = find_xmas_in_x(file_data)
    print(f'Find Keyword X-MAS in "X" shape {X_results} times.')
    