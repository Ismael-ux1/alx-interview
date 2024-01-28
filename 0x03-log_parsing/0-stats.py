#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
"""

# Import necessary modules
import sys
import signal
import re

# Initialize variables for total size, status codes, and line count
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


# Define the format of the log line using a regular expression
log_format = re.compile(
    r'(\S+) - \[(.+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
)


def print_stats():
    """
    This function prints the total file size and the count of each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """
    This function handles keyboard interruption (CTRL + C).
    It prints the current statistics and exits the program.
    """
    print_stats()
    sys.exit(0)


# Set up the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
for line in sys.stdin:
    match = log_format.match(line)
    if match:
        # If the line matches the log format,
        # update total file size and status code count
        total_size += int(match.group(4))
        status_code = int(match.group(3))
        if status_code in status_codes:
            status_codes[status_code] += 1

    line_count += 1
    # Print stats every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print final stats
print_stats()
