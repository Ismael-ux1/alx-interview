#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys
import signal
import re

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Define the format of the log line
log_format = re.compile(
    r'(\S+) - \[(.+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
)


def print_stats():
    """
    This function prints the total file size and the count of each status code
    """
    print("Total file size: File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


# Handle keyboard interruption
def signal_handler(sig, frame):
    """
    This function handles keyboard interruption (CTRL + C).
    It prints the current statistics and exits the program.
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
for line in sys.stdin:
    match = log_format.match(line)
    if match:
        # Update total file size
        total_size += int(match.group(4))
        # Update status code count
        status_code = int(match.group(3))
        if status_code in status_codes:
            status_codes[status_code] += 1
    line_count += 1
    # Print stats every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print final stats
print_stats()
