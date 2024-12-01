from collections import deque

def search(graph, name):
    """Find the man selling mango using BFS"""
    # Define a double-ended queue
    search_queue = deque()
    
    # Put the starting node in the deque
    search_queue += graph[name]
    
    # Created a list to store searched nodes
    searched = []
    
    # Do while the deque isnot empty
    while search_queue:
        # Pop the left(1st) node 
        person = search_queue.popleft()
        
        # If person isnot been searched before
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
    
def person_is_seller(name):
    return name[-1] == 'm'

# Example usage:
# Create a graph using hash table:
graph           = {}
graph["you"]    = ["alice", "bob", "claire"]
graph["bob"]    = ["anuj", "peggy"]
graph["alice"]  = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"]   = []
graph["peggy"]  = []
graph["thom"]   = []
graph["jonny"]  = []

search(graph, "you")