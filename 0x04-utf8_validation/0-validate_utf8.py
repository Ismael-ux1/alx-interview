#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ A function that represents a valid UTF-8 encoding. """

    # Initialize a counter for the bytes to process
    bytes_to_process = 0

    # Iterate over each number in the data list
    for num in data:
        # Convert the number to binary,
        # keeping only the least significant 8 bits
        num = format(num, '#010b')[-8:]

        # If we're not currently processing a character
        if bytes_to_process == 0:
            # Count the number of leading 1s in the current byte
            for bit in num:
                if bit == '0':
                    break
                bytes_to_process += 1

            # If the byte doesn't start with 1s, skip to the next byte
            if bytes_to_process == 0:
                continue

            # If the byte starts with more than 4 1s or only 1 1,
            # it's not a valid UTF-8 character
            if bytes_to_process == 1 or bytes_to_process > 4:
                return False
        else:
            # If we're processing a character,
            # the current byte should start with '10'
            if not (num[0] == '1' and num[1] == '0'):
                return False

        # Decrement the counter after processing a byte
        bytes_to_process -= 1

    # If we've processed all bytes and there are no leftover bytes,
    # the data is valid UTF-8
    return bytes_to_process == 0
