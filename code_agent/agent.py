from google.adk.agents import Agent
from google.adk.code_executors import BuiltInCodeExecutor

root_agent = Agent(
    name="code_agent",
    code_executor=BuiltInCodeExecutor(),
    model="gemini-2.5-flash",
    instruction="사용자가 원하는 파이썬 코드를 작성하고 실행 결과를 알려줘.",
)
