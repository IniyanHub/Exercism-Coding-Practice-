def tick(matrix):
    """
    Advances the game of life by one generation.
    Returns a new matrix representing the next state.
    """
    # Handle edge case for empty board
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new board to store the next state so we don't modify
    # the input while we are still reading from it.
    next_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Directions for the 8 neighbors (row_offset, col_offset)
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            
            # Count live neighbors
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                
                # Check if the neighbor coordinate is valid (within bounds)
                if 0 <= nr < rows and 0 <= nc < cols:
                    live_neighbors += matrix[nr][nc]
            
            # Apply Conway's Rules
            
            # Rule 1 & 3: Any live cell with fewer than 2 or greater than 3 
            # live neighbors dies.
            # Rule 2: Any live cell with 2 or 3 live neighbors lives on.
            if matrix[r][c] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    next_matrix[r][c] = 1
                # else it stays 0 (dead)
            
            # Rule 4: Any dead cell with exactly 3 live neighbors becomes a live cell.
            else:
                if live_neighbors == 3:
                    next_matrix[r][c] = 1
                    
    return next_matrix