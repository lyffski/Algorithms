def ggt_ext(a, b, x, y):
   # default
   if a == 0 :
      x = 0
      y = 1
      return b
   x1 = 1
   y1 = 1
   ggt = ggt_ext(b%a, a, x1, y1)
   # Update x and y with prev. values
   x = y1 - (b/a) * x1
   y = x1
   return ggt

x, y, a, b = 1, 1, 11, 15
ggt = ggt_ext(a, b, x, y)
