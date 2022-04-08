from typing import Dict # type : ignore

factorial_table : Dict ={}  

def factorial(n):
    if n <= 0:
        factorial_table[0] = 1
        return 1
    else:
        factorial_table[n] = n * factorial(n - 1)
        return factorial_table[n]


def main():
    print(factorial(5))


if __name__ == '__main__':
    main()
