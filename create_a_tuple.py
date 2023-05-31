if __name__ == '__main__':

    # read the values of n
    n = int(input())

    n = list(map(int, input().split()))
    # create a tuple
    t = tuple(map(int, n))
    print(hash(t))
