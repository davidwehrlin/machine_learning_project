
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
        return f"height: {self.height}, width: {self.width} \nintersections: {self.the_inte} \ngrid: {self.the_grid}"
    
    def __getitem__(self, key):
        """
            key: a tuple of the intersection

            returns the intersection
        """
        return [x for x in self.the_inte if x.get_name() == key][0]

class Intersection:
    """
    An intersection is the base of the city, it has 4 queues moving from it
    
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
        NorthBound, SouthBount, etc.
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

class Car:
    """
    A car should have a starting location, 
    a destination that is different
    and a route to get there.
    """
    def __init__(self):
        # A tuple of where to start/end
        self.starting = Car.random_location()
        ending_attempt = Car.random_location()
        # While the ending loc isn't the starting
        while ending_attempt != self.starting:
            # Repeatedly create new location
            ending_attempt = Car.random_location()
        # Above is technically O(infinity), whatevs
        # When it is different assign it
        self.ending = ending_attempt
        # list of tuples with start/end
        self.route = Car.generate_route(self.starting, self.ending)
    
    def random_location():
        # Generate random location
        # TODO: define starting location standard
        # TODO: generate a random location
        return (0,0)
    
    def generate_route(start, end):
        # Generate a list of tuples describing path
        route = [start]
        # Generate one of shortest routes in O(HEIGHT + WIDTH)
        # TODO: find shortest route and add it to list
        # Return route with end at the end.
        return route.append(end)
    
    def get_route(self):
        return self.route


def main():
    city = City(HEIGHT, WIDTH)
    print(city)

main()

