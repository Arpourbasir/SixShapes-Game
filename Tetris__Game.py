import tkinter as tk
import random

WIDTH = 330
HEIGHT = 660
GRID_SIZE = 30
COLUMNS = WIDTH // GRID_SIZE
ROWS = HEIGHT // GRID_SIZE

SHAPES = {
    'I': {'color': 'white' , 'shape': [[1, 1, 1, 1]]} ,
    'O': {'color': 'yellow' , 'shape': [[1, 1] , [1, 1]]} ,
    'T': {'color': 'pink' , 'shape': [[0, 1, 0] , [1, 1, 1]]} ,
    'S': {'color': 'green' , 'shape': [[0, 1, 1] , [1, 1, 0]]} ,
    'Z': {'color': 'red' , 'shape': [[1, 1, 0] , [0, 1, 1]]} ,
    'J': {'color': 'blue' , 'shape': [[1, 0, 0] , [1, 1, 1]]} ,
    'L': {'color': 'orange' , 'shape': [[0, 0, 1] , [1, 1, 1]]}
}

def rotate(shape) :
    return [list(row) for row in zip(*shape[::-1])]

class Tetris :
    def __init__(self , master) :
        self.master = master
        self.master.title("بازی تتریس")
        self.game_active = True

        self.start_window = tk.Toplevel(self.master)
        self.start_window.title("شروع بازی")
        self.start_label = tk.Label(self.start_window, text="به بازی تتریس خوش آمدید", font=("Helvetica", 16))
        self.start_label.pack(pady=20)
        self.start_button = tk.Button(self.start_window, text="شروع بازی", command=self.start_game)
        self.start_button.pack(pady=10)


    def start_game(self) :
        self.start_window.withdraw()
        self.master.deiconify()
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack()

        self.canvas = tk.Canvas(self.main_frame, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.grid(row=0, column=0)

        for x in range(0 , WIDTH , GRID_SIZE) :
            self.canvas.create_line(x , 0 , x , HEIGHT , fill="white")
        for y in range(0 , HEIGHT , GRID_SIZE) :
            self.canvas.create_line(0 , y , WIDTH , y , fill="white")

        self.side_panel = tk.Frame(self.main_frame , padx=10)
        self.side_panel.grid(row=0 , column=1 , sticky="n")

        self.level_label = tk.Label(self.side_panel , text="سطح: آسان" , font=("Helvetica", 12))
        self.level_label.pack(pady=10)

        self.score_label = tk.Label(self.side_panel , text="امتیاز: 0" , font=("Helvetica", 12))
        self.score_label.pack(pady=10)

        self.timer_label = tk.Label(self.side_panel , text="زمان: 0" , font=("Helvetica", 12))
        self.timer_label.pack(pady=10)

        self.restart_button = tk.Button(self.side_panel , text="شروع مجدد" , command=self.restart_game)
        self.restart_button.pack(pady=20)

        self.grid = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]

        self.score = 0
        self.level = 'easy'
        self.speed = 750
        self.timer = 0

        self.current_shape = None
        self.shape_x = 0
        self.shape_y = 0

        self.master.bind("<Key>" , self.key_handler)

        self.spawn_shape()
        self.update_timer()
        self.drop()


    def game_over(self) :
        self.canvas.delete("all")
        self.canvas.create_text(WIDTH // 2 , HEIGHT // 2 , text="بازی به پایان رسید" , fill="white" , font=("Helvetica", 20))
        self.game_active = False


    def restart_game(self) :
        self.canvas.delete("all")
        for x in range(0 , WIDTH, GRID_SIZE) :
            self.canvas.create_line(x , 0 , x , HEIGHT , fill="white")
        for y in range(0 , HEIGHT , GRID_SIZE) :
            self.canvas.create_line(0 , y , WIDTH , y , fill="white")
        self.grid = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.score = 0
        self.level = 'easy'
        self.speed = 750
        self.timer = 0
        self.level_label.config(text="سطح: آسان")
        self.score_label.config(text="امتیاز: 0")
        self.timer_label.config(text="زمان: 0")
        self.game_active = True
        self.spawn_shape()


    def update_timer(self) :
        if self.game_active :
            self.timer += 1
            self.timer_label.config(text=f"زمان: {self.timer}")
            self.master.after(1000 , self.update_timer)


    def spawn_shape(self) :
        if not self.game_active :
            return
        self.current_type = random.choice(list(SHAPES.keys()))
        self.current_shape = SHAPES[self.current_type]['shape']
        self.current_color = SHAPES[self.current_type]['color']
        self.shape_y = 0
        self.shape_x = COLUMNS // 2 - len(self.current_shape[0]) // 2


    def key_handler(self , event) :
        if not self.game_active :
            return
        if event.keysym == 'Left' :
            if not self.collision(-1 , 0) :
                self.shape_x -= 1
        elif event.keysym == 'Right' :
            if not self.collision(1 , 0) :
                self.shape_x += 1
        elif event.keysym == 'Down' :
            if not self.collision(0 , 1) :
                self.shape_y += 1
        elif event.keysym == 'Up' :
            rotated = rotate(self.current_shape)
            if not self.collision(0 , 0 , rotated) :
                self.current_shape = rotated
        self.draw()


    def collision(self , dx , dy , shape=None) :
        if shape is None:
            shape = self.current_shape
        for y , row in enumerate(shape) :
            for x , cell in enumerate(row) :
                if cell:
                    nx = self.shape_x + x + dx
                    ny = self.shape_y + y + dy
                    if nx < 0 or nx >= COLUMNS or ny >= ROWS or (ny >= 0 and self.grid[ny][nx]):
                        return True
        return False


    def freeze(self) :
        for y , row in enumerate(self.current_shape) :
            for x , cell in enumerate(row) :
                if cell :
                    gx = self.shape_x + x
                    gy = self.shape_y + y
                    if 0 <= gx < COLUMNS and 0 <= gy < ROWS :
                        self.grid[gy][gx] = self.current_color
        self.clear_lines()
        self.spawn_shape()
        if self.collision(0 , 0) :
            self.game_over()


    def clear_lines(self) :
        lines = 0
        new_grid = []
        for row in self.grid :
            if all(row):
                lines += 1
            else:
                new_grid.append(row)
        for _ in range(lines) :
            new_grid.insert(0 , [None for _ in range(COLUMNS)])
        self.grid = new_grid
        self.score += lines
        self.score_label.config(text=f"امتیاز: {self.score}")
        if self.score >= 60 :
            self.level = 'very hard' 
            self.speed = 150
            self.level_label.config(text="سطح: خیلی سخت")
        elif self.score >= 30 :
            self.level = 'hard'
            self.speed = 300
            self.level_label.config(text="سطح: سخت")
        elif self.score >= 10 :
            self.level = 'medium'
            self.speed = 500
            self.level_label.config(text="سطح: متوسط")


    def drop(self) :
        if not self.game_active :
            return
        if not self.collision(0 , 1) :
            self.shape_y += 1
        else:
            self.freeze()
        self.draw()
        if self.score < 30 and self.game_active :
            self.master.after(self.speed, self.drop)


    def draw(self) :
        self.canvas.delete("piece")
        for y, row in enumerate(self.current_shape) :
            for x, cell in enumerate(row) :
                if cell :
                    x1 = (self.shape_x + x) * GRID_SIZE
                    y1 = (self.shape_y + y) * GRID_SIZE
                    x2 = x1 + GRID_SIZE
                    y2 = y1 + GRID_SIZE
                    self.canvas.create_rectangle(x1 , y1 , x2 , y2 , fill=self.current_color , tags="piece")
        for y , row in enumerate(self.grid) :
            for x , color in enumerate(row) :
                if color :
                    x1 = x * GRID_SIZE
                    y1 = y * GRID_SIZE
                    x2 = x1 + GRID_SIZE
                    y2 = y1 + GRID_SIZE
                    self.canvas.create_rectangle(x1 , y1 , x2 , y2 , fill=color , tags="piece")


root = tk.Tk()
root.withdraw()  
app = Tetris(root)
root.mainloop()
