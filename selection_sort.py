def selection_sort(values):
    n = len(values)
    
    for i in range(n):
        min_i = i

        for j in range(i + 1, n):
            if values[j] < values[min_i]:
                min_i = j

        if min_i != i:
            values[i], values[min_i] = values[min_i], values[i]

    return values