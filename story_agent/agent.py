from google.adk.agents import SequentialAgent, LoopAgent
from .sub_agents import initial_writer_agent, critic_agent, refiner_agent

loop_agent = LoopAgent(
    name="StoryRefinementLoop",
    description="A loop agent that refines a story based on critic feedback.",
    sub_agents=[critic_agent, refiner_agent],
    max_iterations=5,
)

root_agent = SequentialAgent(name="SelfCriticAgent", description="A self-critic writing agent", sub_agents=[initial_writer_agent, loop_agent])
