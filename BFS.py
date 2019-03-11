from collections import deque


def person_is_seller(name):
    return name[-1] == 'm' # check if person name ends with m
    

def search(name):
    search_queue = deque()
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["alice"] = ["peggy"]
    graph["bob"] = ["anuj", "peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"]  = []
    graph["jonny"] = []
    # Implementing breadth first search
    search_queue += graph[name]
    searched = [] # Array for keeping track of those already searched
    while search_queue:
        person = search_queue.popleft()
        if not person in searched: # Only Search this person if you not searched already
            if person_is_seller(person):
                print(person, "is a mango seller!")
                return True
            else:
                search_queue += graph[person] 
                searched.append(person) # Marks this person as searched
        

def main():
    print(search("you"))


if __name__ == "__main__":
    main()