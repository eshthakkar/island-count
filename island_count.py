from collections import deque

def island_count(matrix):
    """Problem: Returns the islands count from the matrix of islands
       Time Complexity: O(nm) where n is the no. of rows and m is the no. of columns in the matrix 

        >>> matrix = [[0, 1, 0, 1, 0],
        ...           [0, 0, 1, 1, 1],
        ...           [1, 0, 0, 1, 0],
        ...           [0, 1, 1, 0, 0],
        ...           [1, 0, 1, 0, 1]]

        >>> print island_count(matrix)
        6

        >>> matrix = [[0, 0, 0, 0],
        ...           [0, 0, 0, 0],
        ...           [0, 0, 0, 0]]

        >>> print island_count(matrix)
        0

        >>> matrix = [[1, 1, 1, 1],
        ...           [1, 1, 1, 1],
        ...           [1, 1, 1, 1]]

        >>> print island_count(matrix)
        1

        >>> matrix = [[1, 0, 0, 1],
        ...           [1, 0, 0, 1],
        ...           [1, 0, 0, 1]]

        >>> print island_count(matrix)
        2

        >>> matrix = [[1, 0, 0, 1],
        ...           [0, 0, 0, 0],
        ...           [1, 0, 0, 1]]

        >>> print island_count(matrix)
        4

        >>> matrix = [[1, 1, 1, 1],
        ...           [1, 0, 0, 1],
        ...           [1, 1, 1, 1]]

        >>> print island_count(matrix)
        1

    """

    rows = len(matrix)
    cols = len(matrix[0])
    islands = 0
    seen = set()
    q = deque()
    potential_neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def add_neighbor(row, col):
        if row < rows and col < cols and row > -1 and col > -1 and (row,col) not in seen and matrix[row][col] == 1:    
            q.append((row,col))
            seen.add((row,col))

    def create_island():
        while q:
            current_index = q.popleft()
            for nei in potential_neighbors:
                add_neighbor(current_index[0] + nei[0], current_index[1] + nei[1])


    for i in xrange(rows):
        for j in xrange(cols):
            if matrix[i][j] == 1 and (i,j) not in seen:
                q.append((i,j))
                seen.add((i,j))
                islands += 1
                create_island()

    return islands 


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. Good WORK!"
    print    




