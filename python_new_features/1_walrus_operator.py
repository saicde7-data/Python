# Without the walrus operator
n = 10
while n > 0:
    print(n)
    n -= 1

# With the walrus operator
n = 10
while (n := n - 1) > 0:
    print(n)