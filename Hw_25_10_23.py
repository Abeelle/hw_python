def sumnub(x):
  s = 0
  while x != 0:
    s += x % 10
    x = x // 10
  print(s)


sumnub(1234)
