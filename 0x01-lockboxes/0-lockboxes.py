#!/usr/bin/python3
""" Determines if all boxes can be opened using the available keys. """


from collections import deque


def canUnlockAll(boxes):
    """
    Args:
        boxes: A list of lists, where each inner list represents a box and,
        contains the keys it holds.

    Returns:
        True if all boxes can be opened, False otherwise.
    """

    # Check for empty or invalid input
    if not boxes or not boxes[0]:
        # Return False for empty or invalid input
        return False
    # Get total number of boxes
    n = len(boxes)
    # Set to keep track of unlocked boxes
    unlocked_boxes = {0}
    # Queue to process boxes
    box_queue = deque([0])

    # Process boxes in the queue
    while box_queue:
        # Dequeue the first box
        current_box = box_queue.popleft()
        # Iterate through keys in the current box
        for key in boxes[current_box]:
            # Check if key is valid and not already unlocked
            if key < n and key not in unlocked_boxes:
                # Add the key to unlocked set
                unlocked_boxes.add(key)
                # Enqueue the corresponding box
                box_queue.append(key)
    return len(unlocked_boxes) == n
