
from queue import Queue
import random
import math

WIDTH = 10
HEIGHT = 10

class LaneQueue:
    queue = []
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size

    def bool_front(self):
        return self.queue[0] is not None

    def get_front(self):
        return self.queue[0]

    def push(self, item):
        if self.queue[self.size - 1] != None:
            raise Error("Queue Overflow")
        else:
            self.queue[self.size - 1] = item



    def pop(self):
        if len(self.queue) == 0:
            raise Error("Queue Empty")
        else:
            temp = self.queue.pop(0)
            self.queue.insert(0, None)
        return temp

    def step(self):
        for i in range(1, len(self.queue)):
            if self.queue[i - 1] == None:
                self.queue[i - 1] = self.queue[i]
                self.queue[i] = None

    def is_full(self):
        return not (None in self.queue)

    def __repr__(self):
        return str(self.queue)



class City:
    """
    The city
    """

    the_grid = {} # Intersections to other Intersections
    the_inte = set() # Set of all the intersections
    time = 0

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

    def step(self): # The city moves everything one step forward
        for inte in the_inte:
            if inte.state == 0:
                moving_lane_bottom = inte.queues[NorthBound()][1]
                moving_lane_top = inte.queues[SouthBound()][1]

                if moving_lane_bottom.bool_front():
                    car = moving_lane_bottom.get_front()
                    if car.peek_direction() is NorthBound() or car.peek_direction() is EastBound():
                        north_inte = the_grid[]
                        east_inte = the_grid[]

            elif inte.state == 1:
                pass
            elif inte.state == 2:
                pass
            elif inte.state == 3:
                pass
            elif inte.state == 4:
                pass
            elif inte.state == 5:
                pass

class Intersection:
    """
    An intersection is the base of the city, it has 4 queues moving from it

    """
    # queues for cars waiting in line
    queues = {}
    # state of intersection
    state = 0

    def __init__(self, x, y):
        # Give the instance an id
        self.x = x
        self.y = y

        # Set the queues for the traffic
        # These are the queues coming into the intersection
        self.queues = {
            NorthBound: (LaneQueue(5), LaneQueue(5)), #[0] is left lane
            SouthBound: (LaneQueue(5), LaneQueue(5)),
            EastBound: (LaneQueue(5), LaneQueue(5)),
            WestBound: (LaneQueue(5), LaneQueue(5)),
        }

        # random
        self.state = random.randint(0,6)

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
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __repr__(self):
        """
        Will return class name when printed
        NorthBound, SouthBount, etc.
        """
        return self.__class__.__name__

    def __str__(self):
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

    def random_location(): #position is a boolean. When it is true it is the start. When it is false it is an end location
        location = (-1, -1)
        #If any of the locations are on the edges of the city use them as the starting location

        while (location[0] != 1
            or location[0] != HEIGHT - 1
            or location[1] != 1
            or location[1] != WIDTH - 1
            or location == (1,1)
            or location == (1,HEIGHT - 1)
            or location == (WIDTH - 1, HEIGHT - 1)
            or location == (WIDTH - 1, 1)):

            location[0] = random.randrange(1, HEIGHT)
            location[1] = random.randrange(1, WIDTH)

        return location

    def get_route(self):
        return self.route

    def peek_direction(self):
        return self.route[1]

    def pop_direction(self):
        return self.route.pop(1)

def generate_route(start, end):
    # Generate a list of tuples describing path

    route = [start]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    while dx != 0 or dy != 0:
        tempdir = random.randint(0,1)
        if tempdir == 0:
            if dx > 0:
                route.append(EastBound())
                dx -= 1
            elif dx < 0:
                route.append(WestBound())
                dx += 1
        elif tempdir == 1:
            if dy > 0:
                route.append(SouthBound())
                dy -= 1
            elif dy < 0:
                route.append(NorthBound())
                dy += 1

    # Generate one of shortest routes in O(HEIGHT + WIDTH)

    # Return route with end at the end.
    route.append(end)
    print(route)
    return route

def main():
    city = City(HEIGHT, WIDTH)
    # print(city)
    generate_route((1,1), (9,9))

main()
