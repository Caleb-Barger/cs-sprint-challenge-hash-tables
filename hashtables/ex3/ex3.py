
ht = {}

def intersection(arrays):

    # given a list of lists (up to 10)
    # find the numbers that appear in all of them

    print(f"BUILDING HASH TABLE")
    for i in range(10000000):
        ht[i] = 0
    print("DONE")

    for a in arrays:
        for n in a:
            if n in ht:
                ht[n] += 1

    items = []

    for k, v in ht.items():
        if v == len(arrays):
            items.append(k)

    return items


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
