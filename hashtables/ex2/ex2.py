#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # populate hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # initialize start point
    route[0] = hash_table_retrieve(hashtable, "NONE")

    # adding the ticket destinations in correct order
    for i in range(1, length - 1):
        route[i] = hash_table_retrieve(hashtable, route[i - 1])

    # remove last value from route because it is always None
    route.pop()
    return route

