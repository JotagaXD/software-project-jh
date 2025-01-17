from utils.ssl.Navigation import Navigation
from utils.ssl.base_agent import BaseAgent
import closer
from time import sleep

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
            target_velocity, target_angle_velocity = Navigation.goToPoint(self.robot, self.targets[self.selection])   
            self.set_vel(target_velocity)
            self.set_angle_vel(target_angle_velocity)

        return

    def post_decision(self):
        pass
