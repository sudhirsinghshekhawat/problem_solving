def min_char_deletion(string):
    frequency_count = {}
    pq = []
    deletion_count = 0

    for i in range(len(string)):
        frequency_count[string[i]] = frequency_count.get(string[i], 0) + 1

    c = list(frequency_count.values())
    print(c)

    for ch in frequency_count:
        pq.append(frequency_count[ch])

    pq.sort()

    while pq:
        frequency = pq.pop()
        if not pq:
            return deletion_count
        if frequency == pq[-1]:
            if frequency > 1:
                pq.append(frequency - 1)
            deletion_count += 1
        pq.sort()
    return deletion_count


if __name__ == '__main__':
    str = "abbbcccd"
    print(min_char_deletion(str))
