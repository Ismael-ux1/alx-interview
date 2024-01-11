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
    if not boxes or not boxes[0]:
        return False  # Return False for empty or invalid input
    n = len(boxes)
    unlocked_boxes = {0}  # Set to keep track of unlocked boxes
    box_queue = deque([0])  # Queue to process boxes
    while box_queue:
        current_box = box_queue.popleft()  # Dequeue the first box
        # Iterate through keys in the current box
        for key in boxes[current_box]:
            # Check if key is valid and not already unlocked
            if key < n and key not in unlocked_boxes:
                unlocked_boxes.add(key)  # Add the key to unlocked set
                box_queue.append(key)  # Enqueue the corresponding box
    return len(unlocked_boxes) == n
