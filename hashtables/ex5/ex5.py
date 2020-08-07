# Your code here

ht = {}

def finder(files, queries):

    # get the last items from all the files
    for i in range(len(files)):
        ht[files[i].split('/')[-1]] = i
        # ht[files[i]] = i

    result = []

    for q in queries:
        if q in ht:
            result.append(files[ht[q]])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
