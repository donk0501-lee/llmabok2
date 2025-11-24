from typing_extensions import override
from typing import Callable, Any, AsyncGenerator, List, Optional
from google.adk.agents import BaseAgent, InvocationContext
from google.adk.events import Event
from google.adk.events.event_actions import EventActions
from google.genai.types import ModelContent

def increase(x: int) -> int:
    return x + 1

class LambdaAgent(BaseAgent):
    """
    Agent that wraps a user-provided function and executes it as part of the agent workflow.
    Allows specifying input keys and output key for session state.
    """
    func: Callable[..., Any]
    input_keys: List[str]
    output_key: Optional[str] = None

    @override
    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        inputs = [ctx.session.state.get(key) for key in self.input_keys]
        result = self.func(*inputs)
        yield Event(author=self.name, 
                    invocation_id=ctx.invocation_id, 
                    content=ModelContent(str(result)), 
                    actions=EventActions(state_delta={self.output_key: result} if self.output_key else {}))


root_agent = LambdaAgent(name="IncreaseAgent", func=increase, input_keys=["number"], output_key="number")