
from queue import Queue


class City:
    """
    The city
    """

    the_grid = {} # Intersections to other Intersections

    def __init__(self, height, width):
        self.width = width
        self.height = height

class Intersection:
    """

    """
    queues = {
        "nb": Queue(),
        "sb": Queue(),
        "eb": Queue(),
        "wb": Queue()
    }
    def __init__(self):
        pass
    

def main():
    print("Hello World!")

main()



