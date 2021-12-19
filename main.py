def minimum(arr):
    print(f'minimum = {min(arr)}')
    return min(arr)


def maximum(arr):
    print(f'maximum = {max(arr)}')
    return max(arr)


def sum_(arr):
    print(f'sum = {sum(arr)}')
    return sum(arr)


def multiplication(arr):
    result = 1
    for i in range(len(arr)):
        result *= arr[i]
    print("multiplication = " + str(result))
    return result


def main():
    with open('spawn.txt', 'r') as f:
        arr = [
            int(el) for el in f.readline().split()
        ]
    minimum(arr)
    maximum(arr)
    sum_(arr)
    multiplication(arr)

if __name__ == '__main__':
    main()
