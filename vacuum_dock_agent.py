from vacuum_agent import VacuumAgent

# We will create our new agent starting from
# the agent created during the workshop on Week 2
class VacuumDockAgent(VacuumAgent):
    
    def __init__(self, agent_program):
        super().__init__(agent_program)