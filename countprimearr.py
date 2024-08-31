def counter(arr):
    counter = 0
    for elem in arr:

        if countPrime(elem) and elem != 1:
            counter = counter + 1

    return counter


def countPrime(elem):
    for i in range(2, elem):
        if elem % i == 0:

            return False

    return True


userinput = list(map(int, input("Enter numbers to check separted by space : ").split()))


print(counter(userinput))
