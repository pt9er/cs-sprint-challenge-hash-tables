#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticket_hash = {}
    route = []
    
    for tix in tickets:
        if tix.source == "NONE":
            route.append(tix.destination)
        ticket_hash[tix.source] = tix.destination
        
    current_tix = ticket_hash[route[0]]
    
    count = 1
    
    while count < length:
        route.append(current_tix)
        current_tix = ticket_hash[current_tix]
        count +=1

    return route
