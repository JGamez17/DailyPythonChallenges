def miniMaxSum(arr):

    total = sum(arr)

    min_sum = float('inf')
    max_sum = float('-inf')

    for i in range(5):
        current_sum = total - arr[i]

        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum > max_sum:
            max_sum = current_sum
    print(min_sum, max_sum)

    if __name__ == '__main__':

        arr = list(map(int, input().rstrip().split()))

        miniMaxSum(arr)
