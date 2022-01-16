# if the number is cleanely divisible then it's not a prime number.

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            # not a prime number as it is cleanly divisible
    if is_prime:
        print("it is a prime number")
    else:
        print("it's not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)
