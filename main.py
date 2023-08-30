from curses import *
from data import Data
import argparse
import json

def draw_separator(stdscr, y):
    width = stdscr.getmaxyx()[1]
    separator = "-" * width
    stdscr.addstr(y, 0, separator, A_BOLD)

def main(stdscr):
    stdscr.clear()
    
    start_color()
    init_pair(1, COLOR_RED, COLOR_BLACK)
    init_pair(2, COLOR_BLUE, COLOR_BLACK)

    data_obj = Data(["docker0", "virbr0", "wlp10s0"])
    ip_dict = data_obj.get_all()
    
    row = 0
    draw_separator(stdscr, row)

    row += 1
    stdscr.addstr(row, 0, "Enable/Disable Interfaces:")
    row += 2  # Skip a line

    for interface, ip in ip_dict.items():
        status = "Enabled" if ip != "N/A" else "Disabled"
        if status == "Enabled":
            stdscr.addstr(row, 0, f"[{interface}]", color_pair(1))
            stdscr.addstr(f" {status}", color_pair(2))
            stdscr.addstr(f" {ip}")
        else:
            stdscr.addstr(row, 0, f"[{interface}]", color_pair(1))
            stdscr.addstr(f" {status} {ip}")
        row += 1

    stdscr.refresh()
    stdscr.getkey()

if __name__ == "__main__":
    wrapper(main)
