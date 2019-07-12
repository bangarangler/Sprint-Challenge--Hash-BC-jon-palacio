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
    source = "NONE"

    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    print(hashtable.storage, "1")
    for item in range(length):
        test = hash_table_retrieve(hashtable, source)
        source = test
        route[item] = test

        print(route)

    print(hashtable.storage, "2")

    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, len(tickets))
