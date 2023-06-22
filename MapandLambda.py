# Generate a list of the first N fibonacci numbers
# Then apply the map() and lambda expression to cube each fibonacci number


# complete the lambda function 
cube = lambda x: x ** 3 

# return a list of fibonacci numbers

# The function follows the classic definition of the Fibonacci sequence, where each number is the sum of the two preceding ones:

def fibonacci(n):
    # initialize the fib_list with the first 2 fibonacci numbers
    fib_list = [0,1]
    for i in range(2,n):
        # sums the previous 2 numbers in the sequence 
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list    
   

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))