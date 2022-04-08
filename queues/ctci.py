def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f'moving disk from source {source} to destination {destination}')
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f'moving disk from source {source} to destination {destination}')
    tower_of_hanoi(n - 1, auxiliary, destination, source)


if __name__ == '__main__':
    tower_of_hanoi(3, 'A', 'C', 'B')
