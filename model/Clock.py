import time
import Agent

class Clock:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent: Agent):
        self.agents.append(agent)

    def _start(self, time_stamp: int):
        while (time_stamp != 0):
            print(f"I am the clock of agents {[agent.id for agent in self.agents]} and I have {time_stamp} seconds left")
            time.sleep(1)
            time_stamp -= 1

        self._notify_agents()
    
    def _notify_agents(self):
        """Notifies all registered agents that the countdown has finished.

        This method calls the _check_clock_time method on each agent, allowing them
        to update their state based on the timer's completion.
        """
        for agent in self.agents:
            agent._check_clock_time()
        
            
