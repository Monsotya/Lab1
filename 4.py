capacity = int(input("Enter capacity of a knapsack\n"))
weights = input("Enter a list of weights of each gold bar\n").split()
buffer = [1] + [0] * capacity

# sets the matrix of values
for i in range(len(weights)):
    for j in range(capacity, int(weights[i]) - 1, -1):
        if buffer[j - int(weights[i])] == 1:
            buffer[j] = 1
i = capacity
while buffer[i] == 0:
    i -= 1
print("\nMaximum weight: " + str(i))
