#! /usr/bin/env python3
#
import tkinter as tk
from PIL import Image, ImageDraw

class ObstacleDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("LBM Obstacle Mask Generator")

        self.Nx, self.Ny = 400, 400

        # Internal PIL image to keep track of the exact bitmask (0 = fluid, 1 = solid)
        self.image = Image.new("1", (self.Nx, self.Ny), 0)
        self.draw = ImageDraw.Draw(self.image)

        # Tkinter Canvas for user interaction
        self.canvas = tk.Canvas(root, width=self.Nx, height=self.Ny, bg='black')
        self.canvas.pack(pady=5)

        # Bind mouse events
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        # UI Controls
        self.mode = tk.StringVar(value="free")

        control_frame = tk.Frame(root)
        control_frame.pack(fill=tk.X, pady=5)

        tk.Radiobutton(control_frame, text="Brush (Freehand)", variable=self.mode, value="free").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(control_frame, text="Eraser", variable=self.mode, value="erase").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(control_frame, text="Rectangle", variable=self.mode, value="rect").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(control_frame, text="Ellipse/Circle", variable=self.mode, value="ellipse").pack(side=tk.LEFT, padx=5)

        tk.Button(control_frame, text="Clear All", command=self.clear).pack(side=tk.RIGHT, padx=5)
        tk.Button(control_frame, text="Export Map", command=self.export_mask, bg="green", fg="white").pack(side=tk.RIGHT, padx=5)

        self.start_x = None
        self.start_y = None
        self.current_shape = None
        self.brush_size = 8

    def on_press(self, event):
        self.start_x, self.start_y = event.x, event.y
        if self.mode.get() in ["rect", "ellipse"]:
            # Create a temporary shape on the canvas to preview the drag
            if self.mode.get() == "rect":
                self.current_shape = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, fill="white", outline="white")
            else:
                self.current_shape = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, fill="white", outline="white")

    def on_drag(self, event):
        if self.mode.get() == "free":
            x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
            x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
            self.canvas.create_oval(x1, y1, x2, y2, fill="white", outline="white")
            self.draw.ellipse([x1, y1, x2, y2], fill=1)
        elif self.mode.get() == "erase":
            x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
            x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
            self.canvas.create_oval(x1, y1, x2, y2, fill="black", outline="black")
            self.draw.ellipse([x1, y1, x2, y2], fill=0)
        elif self.mode.get() in ["rect", "ellipse"] and self.current_shape:
            # Update preview shape bounds
            self.canvas.coords(self.current_shape, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, event):
        if self.mode.get() in ["rect", "ellipse"]:
            # Commit the shape to the PIL image map
            bounds = [self.start_x, self.start_y, event.x, event.y]
            if self.mode.get() == "rect":
                self.draw.rectangle(bounds, fill=1)
            else:
                self.draw.ellipse(bounds, fill=1)
            self.current_shape = None

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, self.Nx, self.Ny], fill=0)

    def export_mask(self):
        filename = "lbm_obstacle_map.txt"
        with open(filename, "w") as f:
            for y in range(self.Ny):
                row_str = ""
                for x in range(self.Nx):
                    val = self.image.getpixel((x, y))
                    row_str += "1" if val > 0 else "0"
                f.write(row_str + "\n")
        print(f"Exported successfully to {filename}!")

if __name__ == "__main__":
  root = tk.Tk()
  app = ObstacleDrawer(root)
  root.mainloop()
