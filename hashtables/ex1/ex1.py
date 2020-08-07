ht = {}

def get_indices_of_item_weights(weights, length, limit):

    # given list of weights 
    # and how big the list is 
    # pick 2 weights that add to satisfy the limit
    
    for i in range(length):
        ht[weights[i]] = i

    for i in range(length):
        if limit - weights[i] in ht:
            return (ht[limit - weights[i]], i)
    
    return None
    

# weights = [ 4, 6, 10, 15, 16 ]
# length = 5
# limit = 21

# # print(get_indices_of_item_weights(weights, length, limit))
# print(get_indices_of_item_weights(weights, length, limit))
