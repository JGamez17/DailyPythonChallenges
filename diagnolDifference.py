def diagonalDifference(arr):
    primary_diagonal = 0
    secondary_diagonal = 0
    n = len(arr)

    for i in range(n):
        primary_diagonal += arr[i][i]
        secondary_diagonal += arr[i][n - i - 1]

    return abs(primary_diagonal - secondary_diagonal)
    # The abs() function ensures the result is always positive, no matter the order


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
