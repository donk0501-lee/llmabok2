from typing_extensions import override
from typing import AsyncGenerator, Optional
from google.adk.agents import BaseAgent, InvocationContext
from google.adk.events import Event
from google.adk.events.event_actions import EventActions

class WhileAgent(BaseAgent):
    """
    Custom agent to orchestrate a workflow with a condition.
    This agent runs a sequence of sub-agents while a specified condition is met.
    """
    condition: str
    max_iterations: Optional[int] = None

    @override
    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        running = True
        while running:
            # Evaluate the condition in the context of the session state
            for sub_agent in self.sub_agents:
                running = eval(self.condition, {}, ctx.session.state)
                if not running:
                    break
                
                async for event in sub_agent.run_async(ctx):
                    yield event
        # yield Event(author=self.name, invocation_id=ctx.invocation_id)

