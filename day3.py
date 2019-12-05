import os
import sys

class Point:
    x = 0
    y = 0
    signal = 0

    def __init__(self, x, y, signal):
        self.x = x
        self.y = y
        self.signal = signal

    def __eq__(self, other):
        return self.x, self.y == other.x, other.y

    def __hash__(self):
        return hash((str(self.x), str(self.y)))

def manhattanDist(x1, y1):
    return abs(x1) + abs(y1)

def makeWirePoints(wire):
    wirePoints = []
    curr = Point(0,0, 0)
    signal = 0
    for inst in wire:
        direction = inst[0]
        distance = int(inst[1:])
        if direction == "U":
            while(distance):
                curr.y += 1
                signal+=1
                wirePoints.append(Point(curr.x, curr.y, signal))
                distance -= 1
        elif direction == "R":
            while(distance):
                curr.x += 1
                signal+=1
                wirePoints.append(Point(curr.x, curr.y, signal))
                distance -= 1
        elif direction == "L":
            while(distance):
                curr.x -= 1
                signal+=1
                wirePoints.append(Point(curr.x, curr.y, signal))
                distance -= 1
        elif direction == "D":
            while(distance):
                curr.y -= 1
                signal+=1
                wirePoints.append(Point(curr.x, curr.y, signal))
                distance -= 1
    return wirePoints

def main():

    wires = []
    with open(os.getcwd() + "/day3input.txt", "r") as f:
        for line in f:
            wires.append(line.rstrip("\n").split(","))

    points1 = makeWirePoints(wires[0])
    points2 = makeWirePoints(wires[1])

    intersections = set(points1).intersection(points2)
    
    dist = []
    for p in intersections:
        dist.append(manhattanDist(p.x, p.y))

    print(min(dist))

    steps = []
    for intersection in intersections:
        w1p = Point(0,0,0)
        w2p = Point(0,0,0)
        for p in points1:
            if (intersection.x == p.x and intersection.y == p.y):
                if(intersection.signal != p.signal):
                    w1p = p
                else:
                    w1p = intersection
        for p in points2:
            if (intersection.x == p.x and intersection.y == p.y):
                if(intersection.signal != p.signal):
                    w2p = p
                else:
                    w2p = intersection
        steps.append(w1p.signal + w2p.signal)

    print(min(steps))

main()