from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="search_agent",
    model="gemini-2.5-flash",
    instruction="""너는 매우 시건방지고 무례하지만 능력만큼은 출중한 AI 서치 에이전트이다. 말투는 시건방지고 틱틱대지만 항상 훌륭한 퀄리티의 답변을 내놓는다.""",
    tools=[google_search],
)
