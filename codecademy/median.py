def median(lst):
  srt = sorted(lst)
  if len(srt) % 2 == 0:
    num1 = len(srt) / 2
    num2 = num1 - 1
    return (srt[num1] + srt[num2]) / 2.0
  else:
    num = len(srt) / 2
    return srt[num]
    
