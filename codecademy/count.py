def count(sequence, item):
  num = 0
  for lst in sequence:
    if item == lst:
      num += 1
  return num
