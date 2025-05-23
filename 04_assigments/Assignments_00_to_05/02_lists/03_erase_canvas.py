# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, 
# when dragged around the canvas, sets all of the rectangles it is in contact with to white.


import tkinter as tk

# canvas size
ROWS,COLS = 15,15
CELL_SIZE = 30

class EraserApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Eraser App")

        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg="white")
        self.canvas.pack()

        self.cells  = {}
        self.create_grid()

        self.eraser = self.canvas.create_rectangle(0,0,CELL_SIZE,CELL_SIZE, outline="black", fill="pink")
        self.canvas.bind("<B1-Motion>", self.erase)


    def create_grid(self):
        # Create blue cells
        for row in range(ROWS):
            for col in range(COLS):
                x1,y1 = col * CELL_SIZE, row * CELL_SIZE
                x2,y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                react = self.canvas.create_rectangle(x1,y1,x2,y2, outline="black", fill="blue")
                self.cells[(row,col)] = react

    def erase(self, event):
        """ Erase the Cell under the eraser """
        self.canvas.coords(self.eraser, event.x, event.y, event.x+CELL_SIZE, event.y+CELL_SIZE)

        for (row,col) ,react in self.cells.items():
            x1,y1,x2,y2 = self.canvas.coords(react)
            if event.x >= x1 and event.x <= x2 and event.y >= y1 and event.y <= y2:
                self.canvas.itemconfig(react, fill="white")


root = tk.Tk()
app = EraserApp(root)
root.mainloop()
            
            
                
                    
        
        



# from graphics import GraphWin, Rectangle, Point
# import time

# # Constants
# CANVAS_WIDTH = 400
# CANVAS_HEIGHT = 400
# CELL_SIZE = 40
# ERASER_SIZE = 20

# def erase_objects(canvas, eraser):
#     """Erase objects in contact with the eraser."""
#     mouse_point = canvas.getMouse()
    
#     # Calculate the boundaries of the eraser's current position
#     left_x = mouse_point.getX() - ERASER_SIZE / 2
#     top_y = mouse_point.getY() - ERASER_SIZE / 2
#     right_x = left_x + ERASER_SIZE
#     bottom_y = top_y + ERASER_SIZE
    
#     # Check each cell and erase the ones that overlap with the eraser
#     for obj in canvas.items[:]:
#         if isinstance(obj, Rectangle):
#             p1 = obj.getP1()  # Top-left corner
#             p2 = obj.getP2()  # Bottom-right corner
            
#             rect_left_x, rect_top_y = p1.getX(), p1.getY()
#             rect_right_x, rect_bottom_y = p2.getX(), p2.getY()

#             # Check if there's overlap between the eraser and the cell
#             if (left_x < rect_right_x and right_x > rect_left_x and
#                 top_y < rect_bottom_y and bottom_y > rect_top_y):
#                 obj.setFill('white')  # Erase the cell by setting it to white

# def main():
#     canvas = GraphWin("Canvas Eraser", CANVAS_WIDTH, CANVAS_HEIGHT)
    
#     num_rows = CANVAS_HEIGHT // CELL_SIZE
#     num_cols = CANVAS_WIDTH // CELL_SIZE
    
#     # Draw a grid of blue cells
#     for row in range(num_rows):
#         for col in range(num_cols):
#             left_x = col * CELL_SIZE
#             top_y = row * CELL_SIZE
#             right_x = left_x + CELL_SIZE
#             bottom_y = top_y + CELL_SIZE
            
#             # Create a cell
#             cell = Rectangle(Point(left_x, top_y), Point(right_x, bottom_y))
#             cell.setFill("blue")
#             cell.draw(canvas)
    
#     # Wait for a click to start erasing
#     canvas.getMouse()
    
#     # Create the eraser
#     eraser = Rectangle(Point(0, 0), Point(ERASER_SIZE, ERASER_SIZE))
#     eraser.setFill("pink")
#     eraser.draw(canvas)
    
#     # Move the eraser with the mouse and erase objects
#     while True:
#         mouse_point = canvas.getMouse()
#         eraser.move(mouse_point.getX() - eraser.getCenter().getX(), 
#                     mouse_point.getY() - eraser.getCenter().getY())
        
#         # Erase overlapping objects
#         erase_objects(canvas, eraser)
        
#         time.sleep(0.05)


# if __name__ == "__main__":
#     main()
