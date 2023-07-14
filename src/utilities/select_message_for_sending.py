import time
import random


def read_file_line_by_line(file, strip = False):

    lines = []
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if strip:
        lines = [line.strip() for line in lines]
    return lines

def select_random_msg(file):
  first_messages = read_file_line_by_line(file)
  lengthOfLines = len(first_messages)

  rand = random.randrange(0, lengthOfLines)
  tmp_msg = first_messages[rand]
  start_index = -1
  end_index = -1
  count = 0
  starts = []
  ends = []
  while True:
      start_index = tmp_msg.find("{", start_index + 1)
      end_index = tmp_msg.find("}", end_index + 1)
      if start_index == -1 | end_index == -1:
          break
      starts.append(start_index)
      ends.append(end_index)
      count += 1     
  final_msg = ""
  if(count == 0):
      return tmp_msg
  else:
      for x in starts:
          order = starts.index(x)
          if (order == 0):
              prevsection = tmp_msg[0 :x]
              final_msg += prevsection
          else:
              prevsection = tmp_msg[ends[order-1] + 1: x]
              final_msg += prevsection
          components = tmp_msg[x + 1: ends[order]].split("|")
          components_length = len(components)
          final_msg += components[random.randrange(0, components_length)]
      final_msg += tmp_msg[ends[len(starts)-1] + 1:]
  return final_msg

def update_file(file_path, line_number):
    # Read all lines from the file
    lines = read_file_line_by_line(file_path)

    # Remove the line at the specified line number
    if line_number < 1 or line_number > len(lines):
        print("Invalid line number")
        return

    del lines[line_number - 1]

    # Write the updated lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
