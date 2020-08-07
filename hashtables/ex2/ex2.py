#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


ht = {}

def reconstruct_trip(tickets, length):

    # source is NONE for the first ticket
    # destination is NONE for the last ticket

    for i in range(length):
        ht[tickets[i].source] = tickets[i].destination

    # reconstruct order
    route = [ht["NONE"]]


    for i in range(length):
        if route[i] == "NONE":
            break
        route.append(ht[route[i]])
    
    return route



