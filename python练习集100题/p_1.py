x = 0
for i in range(1,5):
      for j in range(1,5):
            for k in range(1,5):
                  if (i != j) and (i != k) and (j != k):
                        x += 1
                        if x % 4:
                              print("%d%d%d" % (i, j, k), end = ' | ')
                        else:
                             print("%d%d%d" % (i, j, k))
            
