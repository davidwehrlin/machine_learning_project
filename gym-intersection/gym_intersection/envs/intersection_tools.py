import random
import math

class LaneQueue:
    queue = []
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size

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

    def lane_step(self):
        for i in range(1, len(self.queue)):
            if self.queue[i - 1] == None:
                self.queue[i - 1] = self.queue[i]
                self.queue[i] = None

    def is_full(self):
        return not (None in self.queue)

    def __repr__(self):
        return str(self.queue)

class Car:
    def __init__(self, start_time):
        # TODO
        self.start_time = start_time
class Intersection:
    def __init__(self, lanesize):
        self.lanes = [  LaneQueue(lanesize), LaneQueue(lanesize),
                        LaneQueue(lanesize), LaneQueue(lanesize),
                        LaneQueue(lanesize), LaneQueue(lanesize),
                        LaneQueue(lanesize), LaneQueue(lanesize)]
    def inserted_cars(self):
        #TODO
        pass
    def intersection_step(self):
        #TODO
        pass
