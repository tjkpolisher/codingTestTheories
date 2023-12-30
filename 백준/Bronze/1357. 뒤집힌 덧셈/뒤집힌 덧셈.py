X, Y = input().split()
X, Y = X[::-1], Y[::-1]
summation = str(int(X) + int(Y))
print(int(summation[::-1]))