input_list = [[1,'a',['cat'] ,2] ,[[[3]],'dog'] ,4 ,5]
output = []

def flatten(inp: list) -> list:
  """
  Girilen listenin içerisinde, liste varsa, recursive olarak davranıyor.
  """
  for i in inp:
    if isinstance(i, list):
      flatten(i)
    else:
      output.append(i)

  return output

if __name__ == "__main__":
  opt = flatten(input_list)
  print(opt)
