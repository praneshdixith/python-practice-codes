def count_occurrences(x):
    my_list = [0] * 10
    for i in x:
        my_list[i]+=1
    x = 0
    for i in my_list:
        if (i != 0):
            print(f"{x} : {i}")
        x =x+1

# Example usage:
count_occurrences([1, 2, 2, 3, 4, 4, 4, 5, 9])  # Output: {1: 1, 2: 2, 3: 1, 4: 3, 5: 1}