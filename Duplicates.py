
def find_duplicates(val):
    seen = set()
    dup = set()
    for i in val:
        if i in seen:
            dup.add(i)
        else:
            seen.add(i)
    
    return dup


# Example usage:
print(find_duplicates([1, 2, 3, 4, 2, 3, 5, 6]))  # Output: [2, 3]