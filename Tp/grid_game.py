import turtle 
import random
import time

# ---------------- Setup Turtles ----------------
n = turtle.Turtle()
p = turtle.Turtle()
p.hideturtle()
p.penup()
p.goto(350,150)    
p.color("white")
p.write("Leaderboard" , font = ("Arial" , "20"))

history = []        # store player moves
redo_stack = []     # store undone moves for redo
paused = False      # stopwatch running
pause_start = None
paused_offset = 0

n.hideturtle()

# ---------------- Screen Setup ----------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

# ---------------- Difficulty Setup ----------------
def scramble_grid(moves):
    grid = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,0]]
    er, ec = 3, 3
    for _ in range(moves):
        possible_moves = []
        if er > 0: possible_moves.append((er-1, ec))
        if er < 3: possible_moves.append((er+1, ec))
        if ec > 0: possible_moves.append((er, ec-1))
        if ec < 3: possible_moves.append((er, ec+1))
        nr, nc = random.choice(possible_moves)
        grid[er][ec], grid[nr][nc] = grid[nr][nc], grid[er][ec]
        er, ec = nr, nc
    return grid

# ---------------- Undo/Redo Buttons ----------------
n.penup()    
n.goto(-430 , 50)
n.pendown()
n.color("white")
n.write("⬅️" , font = ("Arial" , "30")) 

n.penup()    
n.goto(-400 , 50)    
n.pendown()
n.color("white")
n.write("➡️" , font = ("Arial" , "30"))    

# ---------------- Input Name and Difficulty ----------------
name = turtle.textinput("Name","Enter your name")

def choose_difficulty():
    level = turtle.textinput("Difficulty", "Choose difficulty: easy / medium / hard")
    if level and level.lower() == "easy":
        return scramble_grid(50)
    elif level and level.lower() == "medium":
        return scramble_grid(100)
    else:
        return scramble_grid(500)

grid = choose_difficulty()

# ---------------- Moves Counter ----------------
moves = 0
move = turtle.Turtle()
move.hideturtle()
move.penup()
move.goto(300 , 400)
move.color("white")

def update_moves():
    move.clear()
    move.write(f"Moves:{moves}",align="center",font=("Arial","30"))

# ---------------- Pause Button ----------------
w = turtle.Turtle()
w.hideturtle()
w.penup()
w.goto(0,450)
w.fillcolor("red")
w.begin_fill()
for i in range (2):
    w.forward(100)
    w.right(90)
    w.forward (50)
    w.right(90)
w.end_fill()    
w.goto(20,415)
w.write("Pause",font =("Arial" , "20"))         

# ---------------- Timer -----------------------
timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.color("white")
timer.goto(-300 , 400)
start_time = time.time()

def updated_time():
    global paused_offset
    if not paused:  
        new_time = int(time.time() - start_time - paused_offset)
        minutes = new_time//60
        seconds = new_time%60
        timer.clear()   
        timer.write(f"⏱ {minutes:02}:{seconds:02}", align="center", font=("Arial", 30, "bold"))
    turtle.ontimer(updated_time, 1000)

# ---------------- Grid Drawing -----------------
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
colors = ["lavender" , "peachpuff"]

# Instructions
p.penup()
p.goto(-725 , 330)
p.color("white")
p.write("INSTRUCTIONS :-" , font= ("Arial" , 25))
p.penup()
p.goto (-725 , 300)
p.write("Arrange the given numbers in ascending order by swapping the empty block from adjacent ones. Click Pause to stop/resume.", font = ("Arial" , 20))
p.penup()
p.goto(-725 , 265)
p.write("Click on the adjacent block which you want to swap with the empty block.", font = ("Arial" , 20))
p.penup()
p.goto(-725 , 230)
p.write("Click the arrow buttons to undo or redo a move." , font = ("Arial","20"))

def draw_square(x, y, color, num):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    if num != 0:
        t.penup()
        t.goto(x + 50, y + 30)  
        t.write(num, align="center", font=("Arial", 24, "bold"))

def draw_grid():
    t.clear()
    for i in range(4):
        for j in range(4):
            x = -200 + i*100
            y =  100 - j*100
            col = colors[(i + j) % 2]
            draw_square(x, y, col, grid[j][i])  
    screen.update()

def find_empty_cell():
    for r in range(4):
        for c in range(4):
            if grid[r][c]==0:
                return r, c
    return None

def is_adjacent(r1, c1, r2, c2):
    return (r1 == r2 and abs(c1 - c2) == 1) or (abs(r1 - r2) == 1 and c1 == c2)

def check_win():
    solved = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,0]
    ] 
    return grid == solved

# ---------------- Click Handler ----------------
def click_handler(x, y):
    global paused, paused_offset, pause_start, moves

    # Leaderboard display
    if 345 <= x <= 465 and 150 <= y <= 175:   
        paused = True
        screen.clear() 
        screen.bgcolor("black")  
        p.penup()
        p.goto(0, 250)
        p.color("white")
        p.write("🏆 LEADERBOARD 🏆", align="center", font=("Arial", 32, "bold"))

        # Read and sort leaderboard
        try:
            with open("leaderboard.txt", "r") as f:
                entries = f.readlines()
        except FileNotFoundError:
            entries = []

        leaderboard = []
        for line in entries:
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                name_ = parts[0]
                moves_str = parts[1].split()[0]
                try:
                    moves_count = int(moves_str)
                    time_str = parts[2] if len(parts) > 2 else ""
                    leaderboard.append((name_, moves_count, time_str))
                except:
                    continue

        leaderboard.sort(key=lambda x: x[1])

        # Display top 10
        start_y = 200
        y_offset = 30
        for i, (name_, moves_count, time_str) in enumerate(leaderboard[:10]):
            display_line = f"{name_}\t{moves_count} moves\t{time_str}"
            p.goto(-300, start_y - (i * y_offset))
            p.color("white")
            p.write(display_line, align="left", font=("courier", 16, "normal"))
        return

    # Pause/Resume
    if 0 <= x <= 100 and 350 <= y <= 500:
        if not paused:
            paused = True
            pause_start = time.time()
            # Draw resume button
            w.penup()
            w.goto(0,450)
            w.fillcolor("red")
            w.begin_fill()
            for i in range(2):
                w.forward(100)
                w.right(90)
                w.forward(50)
                w.right(90)
            w.end_fill()
            w.goto(17,412)
            w.write("Resume", font=("Arial",20))
        else:
            paused = False
            paused_offset += time.time() - pause_start
            w.penup()
            w.goto(0,450)
            w.fillcolor("red")
            w.begin_fill()
            for i in range(2):
                w.forward(100)
                w.right(90)
                w.forward(50)
                w.right(90)
            w.end_fill()
            w.goto(20,415)
            w.write("Pause", font=("Arial",20))
        return

    if paused:
        return

    # Grid clicks
    col = int((x+200)//100)
    row = int((200-y)//100)
    if 0 <= row < 4 and 0 <= col < 4:
        er, ec = find_empty_cell()
        if is_adjacent(row, col, er, ec):
            grid[er][ec], grid[row][col] = grid[row][col], grid[er][ec]
            draw_grid()
            moves += 1
            update_moves()
            history.append((row, col, er, ec))
            if check_win():
                new_time = int(time.time() - start_time - paused_offset)
                minutes = new_time // 60
                seconds = new_time % 60
                new_entry = f"{name}\t{moves} moves\t{minutes:02}:{seconds:02}\n"

                # Update leaderboard file
                try:
                    with open("leaderboard.txt", "r") as f:
                        entries = f.readlines()
                except FileNotFoundError:
                    entries = []

                entries.append(new_entry)

                leaderboard = []
                for line in entries:
                    parts = line.strip().split("\t")
                    if len(parts) >= 2:
                        name_ = parts[0]
                        moves_str = parts[1].split()[0]
                        try:
                            moves_count = int(moves_str)
                            time_str = parts[2] if len(parts) > 2 else ""
                            leaderboard.append((name_, moves_count, time_str))
                        except:
                            continue

                leaderboard.sort(key=lambda x: x[1])

                with open("leaderboard.txt", "w") as f:
                    for entry in leaderboard:
                        f.write(f"{entry[0]}\t{entry[1]} moves\t{entry[2]}\n")

                w.penup()
                w.goto(-275,-300)
                w.color("green")
                timer.clear()
                w.write(f"Congratulations !! You won !! You took {moves} moves and {minutes:02}:{seconds:02} seconds to solve this",
                        font=("Arial", 20))
                paused = True

    # Undo button
    if -500 <= x <= -400 and 0 <= y <= 100:
        if history:
            fr, fc, tr, tc = history.pop()
            redo_stack.append((fr, fc, tr, tc))
            grid[fr][fc], grid[tr][tc] = grid[tr][tc], grid[fr][fc]
            moves -= 1
            update_moves()
            draw_grid()
            return   

    # Redo button
    if -400 <= x <= -300 and 0 <= y <= 100:
        if redo_stack:
            nr, nc, pr, pc = redo_stack.pop() 
            grid[nr][nc], grid[pr][pc] = grid[pr][pc], grid[nr][nc]
            history.append((nr, nc, pr, pc))
            moves += 1
            update_moves()
            draw_grid()
            return

# ---------------- Run Game ----------------
updated_time()
draw_grid()
screen.onclick(click_handler)
turtle.done()
