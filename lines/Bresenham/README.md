

# Bresenham Algorithm

1. Start
2. Initialize the glut library toolkit
3. Initialize window size and position
4. Read x1, x2, y1, y2
5. 
glutCreateWindow("Bresenham Algorithm")
glutDisplayFunc(bresenham)
glutMainLoop()
6. Create redrawing function bresenham()
    def bresenham():
    Set pixel(x1, y1)
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    if dx > dy:
    p = (2 * dy) - dx
    y = y1
    for x in range(x1 + 1, x2 + 1):
    if p < 0:
    p += 2 * dy
    else:
    p += (2 * dy) - (2 * dx)
    y += 1
    Set pixel(x, y)
    else:
    Perform same process for y instead of x

7. Stop