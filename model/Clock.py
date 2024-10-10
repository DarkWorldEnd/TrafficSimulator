import time
from model import Agent

class Clock:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent: Agent):
        self.agents.append(agent)

    def _start(self, time_stamp: int):
        seconds = 0
        while seconds < time_stamp:
            seconds += 1
            print("time_stamp",time_stamp)
            print(f"Clock is ticking {seconds}")
            if seconds == time_stamp:
                self._notify_agents()
            time.sleep(1)
    
    def _notify_agents(self):
        """Notifies all registered agents that the countdown has finished.

        This method calls the _check_clock_time method on each agent, allowing them
        to update their state based on the timer's completion.
        """
        for agent in self.agents:
            agent._check_clock_time()
        
            
