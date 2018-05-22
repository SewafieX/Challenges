# result = n + nn + nnn
# if n = 5 then result = 5 + 55 + 555
n = int(input("n is: "))
n1 = int("%s" % n)
n2 = int("%s%s" % (n, n))
n3 = int("%s%s%s" % (n, n, n))
result = n1 + n2 + n3
print(result)