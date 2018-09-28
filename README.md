
# Multi-Agent Reinforcement Learning for Traffic Light Control
## Machine Learing Project

## Paper

A theory based project where an agent manages traffic in a simple city and is reinforced to allow better traffic flow.
[Paper can be found here.](https://dspace.library.uu.nl/bitstream/handle/1874/20827/wiering_00_multi.pdf?sequence=2)

The city is a graph where the nodes are intersections and the roads are queues with a fixed length of 5. 

## People

|Author|Email|
|---|---|
|Derek Foundoulis|foundoulis@mines.edu|
|Author 2|   |
|Author 3|   |

## TODO

In the short run:
- Finish car class.
- Make city spawn car to intersection.
- Expand intersection to handle cars moving forward in queue.
- Change the code to match the python modules thing. Not just one giant file. 

In the long run:
- Start the actual machine learning part

## Documentation

Global Variables:

- WIDTH: width of the city by intersection.
- HEIGHT: height of the city by intersection.

### City Class

Attributes:

- the_grid: A map of intersections that maps to another intersection.
- the_inte: A set of all the intersections
- width: width of the number of intersections
- height: height of the numer of intersections

Functions:

- __init__: takes height and width and initializes the city class, creates intersections, and maps them to the neighbooring ones.
- __str__: prints the height, width, the_grid, and the_inte.
- __getitem__: returns the intersection at a given key (which is a tuple).

A class that models the city itself, will need an interface for the agent to control and a discrete time system.

### Intersection Class

Attributes: 

- queues: map of directions to the queues of the cars in that lane. All queues are inbound to the intersection
- x, y: location of the intersection in the city.

Functions:

- get_name: returns a tuple of the intersections location
- __repr__: returns string tuple with location

### Direction and it's childre

Attributes: 

- instance: only one instance to save memory. 

Functions:

- __new__: creates a single instance of the class, makes it so they are always ==
- __repr__: returns the name of the class

### Car Class

Attributes:

- starting: starting location for the car spawn
- ending: destination of the car

Functions:

- __init__: create a new car and giv it a starting location, an ending location and the route to get there. Starting location != ending location. 
- random_location: generate a random location on the map.
- generate_route: given a starting and ending location, generate a shortest route between them. 
