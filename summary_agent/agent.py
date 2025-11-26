from google.adk.agents import Agent
from google.adk.tools import AgentTool

summarizer = Agent(
    name="summarizer",
    model="gemini-2.5-flash",
    description="Agent to summarize text",
    instruction="주어진 내용을 간결하게 요약하십시오.",
)

root_agent = Agent(
    name="summary_agent",
    model="gemini-2.5-flash",
    instruction="입력에 대한 요약이 필요한 경우 'summarizer' 하위 에이전트를 사용하십시오.",
    sub_agents=[summarizer],
)
