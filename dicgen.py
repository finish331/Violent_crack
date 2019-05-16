import itertools as its
words = "0123456789"
dic = open("dictionary.txt", "a")
for i in range(1, 8):
    r = its.product(words, repeat=i)
    for j in r:
        dic.write("".join(j))
        dic.write('\n')

dic.close()
