def isMonotonic(array):
    increasing = True
    decreasing = True
    for i in range(1,len(array)):
        if array[i] > array[i-1] or increasing == True:
            decreasing = False

        if array[i] < array[i-1] or decreasing == True:
            increasing = False
    return increasing or decreasing
    
if __name__ == '__main__':
    array  = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
    result = isMonotonic(array)
    print(result)

	
