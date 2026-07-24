#!/usr/bin/env python3

'''
OPS445 Assignment 2 - Summer 2026
<<<<<<< ours

=======
>>>>>>> theirs
Program: assignment2.py 
Author: Asia Karki
The python code in this file is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

<<<<<<< ours
Date:July 24,2026
=======
Date:July 17,2026
>>>>>>> theirs

'''

import argparse
import os, sys

def parse_command_args() -> object:
    """Set up argparse here. Call this function inside main."""
    parser = argparse.ArgumentParser(
        description="Memory Visualiser -- See Memory Usage Report with bar charts",
        epilog="Copyright 2023"
    )

    parser.add_argument(
        "-H",
        "--human-readable",
        action="store_true",
        help="Prints sizes in human readable format"
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=20,
        help="Specify the length of the graph. Default is 20."
    )

    parser.add_argument(
        "program",
        nargs="?",
        help="if a program is specified, show memory use of all associated processes. Show only total use if not."
    )

    return parser.parse_args()

def percent_to_graph(percent, total_chars):
  # Calculate how many '#' characters to display
    hash_count = int(percent * total_chars)

    # The remaining characters will be spaces
    space_count = total_chars - hash_count

    # Return the completed graph string
    return "#" * hash_count + " " * space_count


def get_sys_mem():
# Open the system memory information file
    with open("/proc/meminfo", "r") as mem_file:
        for line in mem_file:
# Find the line containing the total memory
            if line.startswith("MemTotal:"):
                parts = line.split()
   # Return the memory value as an integer
                return int(parts[1])


def get_avail_mem():
  # Variables used for WSL fallback if MemAvailable is missing
    mem_free = 0
    swap_free = 0
  # Open the system memory information file
    with open("/proc/meminfo", "r") as mem_file:
        for line in mem_file:
# Return MemAvailable if it exists
            if line.startswith("MemAvailable:"):
                parts = line.split()
                return int(parts[1])
     # Save MemFree value
            elif line.startswith("MemFree:"):
                parts = line.split()
                mem_free = int(parts[1])

            elif line.startswith("SwapFree:"):
                parts = line.split()
                swap_free = int(parts[1])

    return mem_free + swap_free
def pids_of_prog(app_name: str) -> list:
    """Given an app name, return all pids associated with app."""

    output = os.popen(f"pidof {app_name}").read().strip()

    if output == "":
        return []

    return output.split()

def rss_mem_of_pid(proc_id: str) -> int:
    """Given a process id, return the Resident memory used."""

    total_rss = 0

    with open(f"/proc/{proc_id}/smaps", "r") as file:
        for line in file:
            if line.startswith("Rss:"):
                total_rss += int(line.split()[1])

    return total_rss

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # iB indicates 1024
    suf_count = 0
    result = kibibytes 
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:  # not program name is specified.
        pass
    else:
        pass
