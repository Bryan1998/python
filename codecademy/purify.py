def purify(x):
  lst = list(x)
  for i in range(len(lst)):
    if not(x[i] % 2 == 0):
      lst.remove(x[i])
  return lst
