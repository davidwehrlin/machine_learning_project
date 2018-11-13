import random
import math
import numpy as np

class LaneQueue:
    queue = []
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size

    def get_front(self):
        return self.queue[0]

    def get(self, i):
        if i > self.size:
            raise Error("Out of bounds.")
        return self.queue[i]

    def exists(self, i):
        if self.get(i) is not None:
            return "@"
        return "-"

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

    def lane_step(self):
        for i in range(1, len(self.queue)):
            if self.queue[i - 1] == None:
                self.queue[i - 1] = self.queue[i]
                self.queue[i] = None

    def is_full(self):
        return not (None in self.queue)

    def draw_lane(self):
        lane = ""
        for spot in self.queue:
            if spot != None:
                lane += "@"
            else:
                lane += "-"
        return lane

    def reverse_draw(self):
        str = ""
        for i in self.draw_lane():
            str = i + str
        return str

    def __repr__(self):
        return str(self.queue)

class Car:
    def __init__(self, start_time):
        # TODO
        self.start_time = start_time

MAP = [
    "              +---------------+              ",
    "              |   |   |       |              ",
    "              |   |   |       |              ",
    "              |   |   |       |              ",
    "              |   |   |       |              ",
    "              |   |   |       |              ",
    "__ __ __ __ __                 __ __ __ __ __",
    "                                             ",
    "                               __ __ __ __ __",
    "                                             ",
    "__ __ __ __ __                 __ __ __ __ __",
    "                                             ",
    "__ __ __ __ __                               ",
    "                                             ",
    "__ __ __ __ __                 __ __ __ __ __",
    "              |       |   |   |              ",
    "              |       |   |   |              ",
    "              |       |   |   |              ",
    "              |       |   |   |              ",
    "              |       |   |   |              ",
    "              +---------------+              ",
]
class Intersection:
    def __init__(self, lanesize):
        self.lanes = [  LaneQueue(lanesize), LaneQueue(lanesize),
                        LaneQueue(lanesize), LaneQueue(lanesize),
                        LaneQueue(lanesize), LaneQueue(lanesize),
                        LaneQueue(lanesize), LaneQueue(lanesize)]
    def draw_intersection(self):
        rows = []
        five_spaces = " " * 5
        seven_spaces = " " * 7
        nine_spaces = " " * 9
        for i in range(5):
            new_row = five_spaces + self.lanes[0].exists(4-i) + self.lanes[1].exists(4-i) + seven_spaces
            rows.append(new_row)
        for i in range(2):
            new_row = nine_spaces + self.lanes[i + 2].draw_lane()
            rows.append(new_row)
        for i in range(2):
            new_row = self.lanes[i + 4].reverse_draw() + nine_spaces
            rows.append(new_row)
        for i in range(5):
            new_row = seven_spaces + self.lanes[0].exists(i) + self.lanes[1].exists(i) + five_spaces
            rows.append(new_row)

        for row in rows:
            print(row)

    def intersection_step(self):
        for lane in self.lanes:
            lane.lane_step()
    def add_cars(self, current_step):
        rand_lane = np.random.randint(2, size=8)
        for i in range(len(self.lanes)):
            if rand_lane[i] == 0:
                self.lanes[i].push(Car(current_step))
                print("Added car to lane ", i, "with a time of ", current_step, ".\n")
