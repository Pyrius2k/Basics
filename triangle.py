def draw_triangle(g):
    """
    Draws an inverted triangle made of asterisks.
    
    Args:
        g (int): The size of the triangle (number of rows).
    """

    for i in range(g, 0, -1):
  
        for _ in range(i):
            print('*', end='')
        print()  


draw_triangle(12)
