#!/usr/bin/python3
  """function determining if all boxes can be opened.

  Args:
    boxes: A list of lists of boxes and corresponding keys.

  Returns:
    True if all boxes can be opened, False otherwise."""
  def canUnlockAll(boxes):
    num_boxes = len(boxes)
    opened_boxes = {0}
    keys = set(boxes[0])

    while keys:
        new_keys = set()
        for key in keys:
            if key < num_boxes and key not in opened_boxes:
                opened_boxes.add(key)
                new_keys.update(boxes[key])
        keys = new_keys
    if len(opened_boxes) == num_boxes:
      return True
    else:
      return False
    