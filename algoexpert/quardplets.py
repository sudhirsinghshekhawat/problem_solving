def quardlets_sum(array, targetSum):
    allPairSum = {}
    quadruplets = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSum:
                for pair in allPairSum[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum in allPairSum:
                allPairSum[currentSum].append([array[i], array[k]])
            else:
                allPairSum[currentSum] = [[array[i], array[k]]]
    return quadruplet


if __name__ == '__main__':
    arr = [-1, 17, 2, 13, 16, 12, 8, 9, 3, 11, 5]
    result = quardlets_sum(arr, 25)
    print(result)
