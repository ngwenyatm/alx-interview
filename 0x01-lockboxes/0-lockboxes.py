#!/usr/bin/python3
  """function determining if all boxes can be opened.
  Args:
    boxes: A list of lists of boxes and corresponding keys.
  Returns:
    True if all boxes can be opened, False if otherwise.
  """
def canUnlockAll(boxes):
  box_n = len(boxes)
  opened_boxes = set([0])
  keys = set(boxes[0])

  while keys:
    temp_keys = set()
    for key in keys:
      if key < box_n and key not in opened_boxes:
        opened_boxes.add(key)
        temp_keys.update(boxes[key])
    keys = temp_keys

  return len(opened_boxes) == box_n
