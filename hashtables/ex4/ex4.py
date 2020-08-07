ht = {}
def has_negatives(a):

    result = []

    for n in a:
        if n != 0:
            ht[n] = 0

    for n in a:
        if n * -1 in ht:
            ht[n] += 1
    
    # print(ht)
    for k, v in ht.items():
        if v >= 1:
            result.append(abs(k))

    if len(result) == 0:
        return []

    return list(set(result))

            

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
