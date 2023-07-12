from vacuum_agent import VacuumAgent

# We will create our new agent starting from
# the agent created during the workshop on Week 2
class VacuumDockAgent(VacuumAgent):
    
    def __init__(self, agent_program):
        super().__init__(agent_program)

    def add_all_sensors(self):
        super().add_all_sensors()
        self.add_sensor('charging-dock-location-sensor', (0,0), lambda v: isinstance (v, tuple) and isinstance (v[0], int) and isinstance (v[0], int))