input_array = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_items(nput_arr: list) -> list:
  """
  a function that splits every item in list and reverses them.
  """
  output_arr = []
  for i in nput_arr:
    output_arr.append(i[::-1])
  
  return output_arr[::-1]

if __name__ == "__main__":
  opt_sec = reverse_items(input_array)
  print(opt_sec)
