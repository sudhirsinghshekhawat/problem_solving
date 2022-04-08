def fizzbuzz(num):
    fizz_count = 0 
    buzz_count = 0 
    fizz_buzz_array = []

    for i in range(1,num+1):
        fizz_count += 1
        buzz_count += 1

        if fizz_count == 3 and buzz_count == 5:
            fizz_buzz_array.append("FizzBuzz")
            fizz_count = 0 
            buzz_count = 0
        elif fizz_count == 3:
            fizz_buzz_array.append("Fizz")
            fizz_count = 0 
        elif buzz_count == 5:
            fizz_buzz_array.append("Buzz")
            buzz_count = 0 
        else:
            fizz_buzz_array.append(str(i))
    return fizz_buzz_array

if __name__ == '__main__':
    result = fizzbuzz(15)
    print(result)

    

