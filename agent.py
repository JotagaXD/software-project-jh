from utils.ssl.Navigation import Navigation
from utils.ssl.base_agent import BaseAgent
from utils.Point import Point
from closer import obstacle
from calculate import angle, distance, linear_coef, angular_coef, relative_x

class ExampleAgent(BaseAgent):
    def __init__(self, id=0, yellow=False):
        super().__init__(id, yellow)

    def decision(self):
        if len(self.targets) == 0:
            return
        
        if self.select == False and len(self.targets) > self.id:
            self.select = True
            self.selection = self.id
        
        if self.select == True:
            destiny = self.targets[self.selection]
            idx_obstacle = obstacle(self, len(self.teammates), len(self.opponents) + 1)
            
            if idx_obstacle != -1:
                self.obstacle = idx_obstacle
                dy = self.targets[self.selection][1] - self.pos[1]
                dx = self.targets[self.selection][0] - self.pos[0]
                n1 = angular_coef(dy, dx)
                n2 = -1/n1
                m1 = linear_coef(n1, self.pos)
                m2 = linear_coef(n2, self.pos)
                theta = angle(n1, dx, dy)
                y1 = n1*self.opponents[self.obstacle].x + m1
                
                if distance((self.opponents[self.obstacle].x, y1), (self.opponents[self.obstacle].x, self.opponents[self.obstacle].y)) < 0.25:
                    x2 = relative_x(y1 < self.opponents[self.obstacle].y, theta, self.pos[0])
                    y2 = n2*x2 + m2
                    destiny = Point(x2, y2)

            target_velocity, target_angle_velocity = Navigation.goToPoint(self.robot, destiny)
            self.set_vel(target_velocity)
            self.set_angle_vel(target_angle_velocity)

        return

    def post_decision(self):
        pass
