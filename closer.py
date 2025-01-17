from utils.Point import Point

def distance(self, i):
    return (((self.my_agents[0].pos[0] - self.targets[i][0])**2) + ((self.my_agents[0].pos[1] - self.targets[i][1])**2))**(1/2)

def sort(self):
    closer_targets = []
    self.targets.append(Point(self.x(), self.y()))
    closer_targets.append(distance(self, 0))
    for i in range(1, self.targets_per_round, 1):
        self.targets.append(Point(self.x(), self.y()))
        closer_targets.append(distance(self, i))
        for j in range(0, i, 1):
            if closer_targets[i] < closer_targets[j]:
                cache1 = self.targets[i]
                cache2 = closer_targets[i]
                for k in range(i, j - 1, -1):
                    self.targets[k] = self.targets[k - 1]
                    closer_targets[k] = closer_targets[k - 1]
                self.targets[j] = cache1
                closer_targets[j] = cache2