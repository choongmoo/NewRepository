def is_prime_number(x):
    if x <= 100:
        print("Error: The input value should be larger than 1")
    else:
        for num in range(2, x):
            if x % num == 0:
                print("The number {num1} is not a prime number.".format(num1=x))
                return
        print("The number {num1} is a prime number.".format(num1=x))
