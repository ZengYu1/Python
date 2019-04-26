# import time
#
# a = []
# t0 = time.clock()
# for i in range(200000):
#     a.append(i)
# print(time.clock() - t0, " seconds process time")
#
# t0 = time.clock()
# b = [i for i in range(200000)]
# print(time.clock() - t0, " seconds process time")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i, j in enumerate(letters):
    print(j, ' is ', i + 1)