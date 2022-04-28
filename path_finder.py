import curses
from curses import wrapper
import queue
import time



maze = [
    ["#", "#", "O", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def view_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, Value in enumerate(row):
            if Value == start:
                return i, j
    return None


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, colm = current_pos
        time.sleep(0.5)
        stdscr.clear()
        view_maze(maze, stdscr, path)
        stdscr.refresh()

        if maze[row][colm] == end:
            return path

        neighbors = find_neighbor(maze, row, colm)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            row1, colm1 = neighbor
            if maze[row1][colm1] == "#":
                continue
            
            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add((neighbor)) 


def find_neighbor(maze, row, colm):
    neighbors = []

    if row > 0:
        neighbors.append((row - 1, colm))
    if row + 1 < len(maze):
        neighbors.append((row + 1, colm))
    if colm > 0:
        neighbors.append((row, colm - 1))
    if colm + 1 < len(maze[0]):
        neighbors.append((row, colm + 1))
    
    return neighbors




def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    ##blue_and_black = curses.color_pair(1)
    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)