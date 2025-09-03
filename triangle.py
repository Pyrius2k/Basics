def draw_triangle(g):
    """
    Draws an inverted triangle made of asterisks.
    
    Args:
        g (int): The size of the triangle (number of rows).
    """
    # Outer loop for the rows, from g down to 1
    for i in range(g, 0, -1):
        # Inner loop for the columns, from 1 to i
        for _ in range(i):
            print('*', end='')
        print()  # Newline after each row

# Example: Draw a triangle with 5 rows
draw_triangle(12)