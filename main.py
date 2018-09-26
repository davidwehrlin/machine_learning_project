
from queue import Queue

WIDTH = 3
HEIGHT = 2

class City:
    """
    The city
    """

    the_grid = {} # Intersections to other Intersections
    the_inte = set() # Set of all the intersections

    def __init__(self, height, width):

        # Dimensions of the city
        self.width = width
        self.height = height

        # Instantiate the intersections
        for x in range(self.width):
            for y in range(self.height):
                # Creates 6 intersections and labels them
                next_intersection = Intersection(x,y)
                self.the_inte.add(next_intersection)
                self.the_grid[next_intersection] = []

        # Map the intersections to eachother
        def directions(x, y):
            """
            Generates the four cardinal directions
            from a given point x,y
            """
            yield x+1, y
            yield x, y+1
            yield x-1, y
            yield x, y-1
        # For every intersection in the city
        for inter in self.the_inte:
            self.the_grid[inter] = []
            # for every direction at that intersection
            for dir_tuple in list(directions(*inter.get_name())):
                # If the coordinates point to a direction that exists
                if dir_tuple[0] >= 0 and dir_tuple[1] >= 0 and dir_tuple[0] < self.width and dir_tuple[1] < self.height:
                    # Add the intersection to the list of neighbors
                    self.the_grid[inter].append(self[(dir_tuple[0], dir_tuple[1])])
        

    def __repr__(self):
        pass
    
    def __str__(self):
        return f"height: {self.height}, width: {self.width}"
    
    def __getitem__(self, key):
        """
            key: a tuple of the intersection

            returns the intersection
        """
        return [x for x in self.the_inte if x.get_name() == key][0]

class Intersection:
    """

    """
    queues = {}

    def __init__(self, x, y):
        # Give the instance an id
        self.x = x
        self.y = y

        # Set the queues for the traffic
        # These are the queues coming into the intersection
        self.queues = {
            NorthBound: Queue(5),
            SouthBound: Queue(5),
            EastBound: Queue(5),
            WestBound: Queue(5)
        }
    
    def get_name(self):
        return (self.x, self.y)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

class Direction:
    instance = None
    def __new__(cls, *args, **kwargs):
        """
        Make sure there is only ever one class in memory
        """
        if cls is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def __repr__(self):
        """
        Will return class name when printed
        """
        return self.__class__.__name__
class NorthBound(Direction):
    pass
class SouthBound(Direction):
    pass
class EastBound(Direction):
    pass
class WestBound(Direction):
    pass

def main():
    city = City(HEIGHT, WIDTH)
    print(city)

main()

