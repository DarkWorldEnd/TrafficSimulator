import time
import threading
from model import Agent

class Clock(threading.Thread):
    def __init__(self):
        self.agents = []
        # self.label = None
        self.seconds = 0

    def add_agent(self, agent: Agent):
        self.agents.append(agent)

    def _start(self, time_stamp: int):
        self.seconds += 1
        print("time_stamp",time_stamp)
        print(f"Clock is ticking {self.seconds}")
        if self.seconds >= time_stamp:
            self.seconds = 0
            self._notify_agents()
    
    def _notify_agents(self):
        """Notifies all registered agents that the countdown has finished.

        This method calls the _check_clock_time method on each agent, allowing them
        to update their state based on the timer's completion.
        """
        for agent in self.agents:
            agent._check_clock_time()
        
            
