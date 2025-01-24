from utils.Point import Point
from calculate import distance

def sort_targets(self):
    closer_targets = []
    self.targets.append(Point(self.x(), self.y()))
    closer_targets.append(distance(self.my_agents[0].pos, self.targets[0]))
    for i in range(1, self.targets_per_round, 1):
        self.targets.append(Point(self.x(), self.y()))
        closer_targets.append(distance(self.my_agents[0].pos, self.targets[i]))
        for j in range(0, i, 1):
            if closer_targets[i] < closer_targets[j]:
                cache1 = self.targets[i]
                cache2 = closer_targets[i]
                for k in range(i, j - 1, -1):
                    self.targets[k] = self.targets[k - 1]
                    closer_targets[k] = closer_targets[k - 1]
                self.targets[j] = cache1
                closer_targets[j] = cache2

def obstacle(self, start, n):
    for i in range(start, n):
        if distance(self.pos, [self.opponents[i].x, self.opponents[i].y]) < 0.20:
            return i
    return -1