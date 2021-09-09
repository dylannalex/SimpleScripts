from math import sqrt


def is_prime(number):
    for n in range(2, int(sqrt(number))):
        if number % n == 0:
            return False
    return True


def main():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print("Your number is prime.")
    else:
        print("Your number is not prime.")


if __name__ == "__main__":
    main()
