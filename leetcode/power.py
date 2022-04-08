def power_int(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        result = power_int(x, n//2)
        return result * result
    else:
        result = power_int(x, (n-1)//2)
        return x * result * result


if __name__ == '__main__':
    output = power_int(2, 4)
    print(f"pow(2,4) : {output}")
    output = power_int(2, 5)
    print(f"pow(2,5) : {output}")
